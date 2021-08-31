![](https://img.shields.io/badge/Status:-RELEASED-green)

## Queue Node Type (Abstract)

Abstract node type representing a message queue independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Queue` | `iaas.nodes.abstract.Queue` | 1.0.0 | `tosca.nodes.Root` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `iaas.capabilities.Invocable` | `iaas.nodes.abstract.Function` | `iaas.relationships.abstract.Triggers` | [0, UNBOUNDED] |
