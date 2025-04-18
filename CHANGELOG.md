# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.7.1] - 2025-04-17

### Fixed

- Fix home URL in chart metadata

## [1.7.0] - 2025-03-31

### Changed

- Upgrade to sloth 0.12.0.

## [1.6.0] - 2025-02-27

### Fixed

- Fix Push to collection CI.

## [1.5.0] - 2025-02-13

### Changed

- Update dashboards for observability-op provisioning.

### Added

- Add helm chart templating test in ci pipeline.
- Add tests with ats in ci pipeline.

## [1.4.5] - 2024-06-12

### Changed

- Add datasource selector to sloth dashboards.

## [1.4.4] - 2024-02-19

### Fixed

- Fix CNP to be able to access DNS.

## [1.4.3] - 2024-02-14

### Fixed

- Fix Cilium Network Policies onprem.

## [1.4.2] - 2024-01-31

### Fixed

- Fix dashboard tags.

## [1.4.1] - 2024-01-31

### Changed

- Rename Sloth dashboards to align with the new SLA reporting dashboard.

## [1.4.0] - 2024-01-29

### Fixed

- Fix issues related to git-sync since upgrade to [4.x.x](https://github.com/kubernetes/git-sync/releases/tag/v4.0.0).

### Changed

- Configure gsoci.azurecr.io as the default container image registry.

## [1.3.0] - 2024-01-23

### Added

- Add `CiliumNetworkPolicy`.

## [1.2.1] - 2023-06-27

### Fixed

- Fix security concerns.

## [1.2.0] - 2023-06-27

### Added

- Add Kyverno Policy Exceptions.

### Changed

- Change image registries to support mirroring.

## [1.1.3] - 2023-06-02

### Added

- Add team label.

### Removed

- Stop pushing to `openstack-app-collection`.

## [1.1.2] - 2023-04-13

## [1.1.1] - 2023-04-11

### Changed

- Updated circleci jobs to push to the `monitoring` namespace in each collection

## [1.1.0] - 2023-04-11

### Added

- Circleci jobs to add sloth to app collections

## [1.0.0] - 2023-04-04

### Changed

- Updated image registry and repository
- Improved readme

### Added

- Automatically generated base files
- Values schema

## [0.11.0-gs2] - 2023-02-20

### Added

- Add modified grafana dashboards.

## [0.11.0-gs1] - 2023-02-20

### Added

- Initial commit with upstream release v0.11.0.

[Unreleased]: https://github.com/giantswarm/sloth-app/compare/v1.7.1...HEAD
[1.7.1]: https://github.com/giantswarm/sloth-app/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/giantswarm/sloth-app/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/giantswarm/sloth-app/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/giantswarm/sloth-app/compare/v1.4.5...v1.5.0
[1.4.5]: https://github.com/giantswarm/sloth-app/compare/v1.4.4...v1.4.5
[1.4.4]: https://github.com/giantswarm/sloth-app/compare/v1.4.3...v1.4.4
[1.4.3]: https://github.com/giantswarm/sloth-app/compare/v1.4.2...v1.4.3
[1.4.2]: https://github.com/giantswarm/sloth-app/compare/v1.4.1...v1.4.2
[1.4.1]: https://github.com/giantswarm/sloth-app/compare/v1.4.0...v1.4.1
[1.4.0]: https://github.com/giantswarm/sloth-app/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/giantswarm/sloth-app/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/giantswarm/sloth-app/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/giantswarm/sloth-app/compare/v1.1.3...v1.2.0
[1.1.3]: https://github.com/giantswarm/sloth-app/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/giantswarm/sloth-app/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/giantswarm/sloth-app/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/giantswarm/sloth-app/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/giantswarm/sloth-app/compare/v0.11.0-gs2...v1.0.0
[0.11.0-gs2]: https://github.com/giantswarm/sloth-app/compare/v0.11.0-gs1...v0.11.0-gs2
[0.11.0-gs1]: https://github.com/giantswarm/sloth-app/compare/v0.0.0...v0.11.0-gs1
