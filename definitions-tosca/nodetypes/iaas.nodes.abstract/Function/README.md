![](https://img.shields.io/badge/Status:-RELEASED-green)

## Function Node Type (Abstract)

Abstract node type representing a serverless function independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Function` | `iaas.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the function |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `iaas.capabilities.Invocable` |   | `iaas.relationships.abstract.Triggers` | [0, UNBOUNDED] |
| `endpoint` | `tosca.capabilities.Endpoint` |   | `tosca.relationships.ConnectsTo` | [0, UNBOUNDED] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `iaas.capabilities.Invocable` |   | [0, UNBOUNDED] |
| `orchestrated` | `iaas.capabilities.Orchestrated` |   | [0, UNBOUNDED] |