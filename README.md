# Briosa Python clients

[Documentation](https://briosa.dev/) | [API Reference](https://briosa.dev/api/python) | [First MP Command](https://briosa.dev/docs/getting-started/first-request)

Independent exact-target clients for the [Briosa SpatialAnalyzer bridge](https://github.com/spatialanalyzer/briosa).

| SpatialAnalyzer target | Product and development guide | Client version |
| --- | --- | --- |
| 2024.1.0508.5 | [SA 2024](targets/2024.1.0508.5/README.md) | 0.5.0 (unreleased) |
| 2026.1.0529.7 | [SA 2026](targets/2026.1.0529.7/README.md) | 0.5.0 (unreleased) |

Choose the package for your exact SA installation. Each product pins its own
generation artifact and retains Server 0.9.2, the newest major-2 server, as the
rejection baseline. The 0.5 client line selects side-by-side servers that
declare behavioral contract major 3 (Server 0.10.0); each product guide lists
its breaking changes under "Contract major 3". Client package versions are
independent of the Briosa server version. See [Releasing](RELEASING.md) for
registry publishing and validation.

Package names include the SA target; application namespaces/imports remain stable.
See each product guide for installation and examples. Run development commands
from the chosen `targets/<exact-sa-release>/` directory. CI validates both products.

SpatialAnalyzer, its SDK, and a license are required separately for real work.
Portable checks do not establish licensed runtime validation. Broader licensed
runtime CI and enterprise Artifactory verification remain outstanding before v1.0
promotion.

The 0.3.0 API naming changes are described in the [MP argument migration guide](docs/mp-argument-name-migration.md).

The default `BriosaStartOptions.startup_timeout` is `120.0` seconds in both
products. It is sized from the server's default lifecycle bounds; see
[startup and lifecycle time budgets](docs/public-api-contract.md#startup-and-lifecycle-time-budgets).
