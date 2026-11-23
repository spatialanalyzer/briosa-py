# Briosa Python clients

[Documentation](https://briosa.dev/) | [API Reference](https://briosa.dev/api/python) | [First MP Command](https://briosa.dev/docs/getting-started/first-request)

Independent exact-target clients for the [Briosa SpatialAnalyzer bridge](https://github.com/spatialanalyzer/briosa).

| SpatialAnalyzer target | Product and development guide | Client version |
| --- | --- | --- |
| 2024.1.0508.5 | [SA 2024](targets/2024.1.0508.5/README.md) | 0.5.0 |
| 2026.1.0529.7 | [SA 2026](targets/2026.1.0529.7/README.md) | 0.5.0 |

Choose the package for your exact SA installation. Client 0.5.x works with
Server 0.10.x (Client 0.5.0 was tested with Server 0.10.0) and does not work
with Server 0.9.x and earlier; clients 0.4.x and earlier do not work with
Server 0.10.x. For server releases after 0.10.0, a patch update keeps the same
clients working; a minor update may require a client upgrade. Each product
pins its own generation artifact and retains Server 0.9.2, the latest 0.9.x
server, as the rejection baseline. Each product guide lists the 0.5.0 breaking
changes under "Upgrading to 0.5.0 (Server 0.10.x)". Client package versions are
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
