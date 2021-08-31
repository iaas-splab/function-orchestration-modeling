![](https://img.shields.io/badge/Status:-RELEASED-green)

## Object Storage Node Type (Abstract)

Abstract node type representing an object storage independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ObjectStorage` | `iaas.nodes.abstract.ObjectStorage` | 1.0.0 | `tosca.nodes.Storage.ObjectStorage` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `iaas.capabilities.Invocable` | `iaas.nodes.abstract.Function` | `iaas.relationships.abstract.Triggers` | [0, UNBOUNDED] |
