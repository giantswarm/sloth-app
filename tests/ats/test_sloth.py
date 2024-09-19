import logging

from typing import List
import yaml
import requests
from pathlib import Path

import pytest
import pykube
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run
from pytest_helm_charts.utils import wait_for_objects_condition

logger = logging.getLogger(__name__)

namespace_name = "monitoring"
deployment_name = "sloth"

timeout: int = 300

prometheusRuleCRDURL = "https://github.com/prometheus-operator/prometheus-operator/blob/main/example/prometheus-operator-crd/monitoring.coreos.com_prometheusrules.yaml"

class PrometheusServiceLevel(pykube.objects.NamespacedAPIObject):
    version = "sloth.slok.dev/v1"
    endpoint = "prometheusservicelevels"
    kind = "PrometheusServiceLevel"

class PrometheusRules(pykube.objects.NamespacedAPIObject):
    version = "monitoring.coreos.com/v1"
    endpoint = "prometheusrules"
    kind = "PrometheusRule"

@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """Very minimalistic example of using the [kube_cluster](pytest_helm_charts.fixtures.kube_cluster)
    fixture to get an instance of [Cluster](pytest_helm_charts.clusters.Cluster) under test
    and access its [kube_client](pytest_helm_charts.clusters.Cluster.kube_client) property
    to get access to Kubernetes API of cluster under test.
    Please refer to [pykube](https://pykube.readthedocs.io/en/latest/api/pykube.html) to get docs
    for [HTTPClient](https://pykube.readthedocs.io/en/latest/api/pykube.html#pykube.http.HTTPClient).
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1

# scope "module" means this is run only once, for the first test case requesting! It might be tricky
# if you want to assert this multiple times
# -- Checking that sloth's deployment is present on the cluster
@pytest.fixture(scope="module")
def deployments(kube_cluster: Cluster) -> List[pykube.Deployment]:
    logger.info("Waiting for sloth to be deployed..")

    deployments = wait_for_deployments(kube_cluster)

    logger.info("sloth is deployed..")

    return deployments

def wait_for_deployments(kube_cluster: Cluster) -> List[pykube.Deployment]:
    deployments = wait_for_deployments_to_run(
        kube_cluster.kube_client,
        [deployment_name],
        namespace_name,
        timeout,
    )
    return (deployments)

# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
# -- Checking that sloth pods are available
@pytest.mark.smoke
@pytest.mark.upgrade
# @pytest.mark.flaky(reruns=5, reruns_delay=10)
def test_sloth_creates_prometheus_rules(kube_cluster: Cluster, deployments: List[pykube.Deployment]):
    # loop over the list of deployments to make sure the pods are running
    for d in deployments:
        assert int(d.obj["status"]["readyReplicas"]) == int(d.obj["spec"]["replicas"])

    sloName = "test-slo"
    logger.info("Creating PrometheusServiceLevel..")
    prometheusservicelevel = {
      "apiVersion": "sloth.slok.dev/v1",
      "kind": "PrometheusServiceLevel",
      "metadata": {
        "name": sloName,
        "namespace": namespace_name,
      },
      "spec": {
        "labels": {
          "owner": "slo",
        },
        "service": "test-service",
        "slos": [
          {
            "alerting": {
              "labels": {
                "team": "slo",
              },
              "name": sloName,
              "pageAlert": {
                "disable": False,
                "labels": {
                  "team": "slo",
                },
              },
              "ticketAlert": {
                "disable": False,
                "labels": {
                  "severity": "notify",
                  "slack_channel": "#team-slo",
                },
              },
            },
            "description": "Test slo",
            "name": sloName,
            "objective": 95,
            "sli": {
              "events": {
                "errorQuery": "avg_over_time(up{cluster_id=\"test\"}[{{.window}}]) > 80",
                "totalQuery": "avg_over_time(up{cluster_id=\"test\"}[{{.window}}])",
              },
            },
          },
        ],
      },
    }
    PrometheusServiceLevel(kube_cluster.kube_client, prometheusservicelevel).create()
    logger.info("PrometheusServiceLevel created..")
    logger.info("Waiting for PrometheusRules to be created..")
    result = wait_for_objects_condition(
      kube_cluster.kube_client,
      PrometheusRules,
      [sloName],
      namespace_name,
      _prometheus_rules_running,
      timeout,
      True,
    )
    logging.info("PrometheusRule created successfully..")
    logging.info(result)
    assert len(result) == 1

def _prometheus_rules_running(rule: PrometheusRules) -> bool:
    complete = (
      "metadata" in rule.obj
    )
    return complete
