![](https://img.shields.io/badge/Status:-RELEASED-green)

## Workflow Node Type (Abstract)

Abstract node type representing a serverless workflow independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Workflow` | `iaas.nodes.abstract.Workflow` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the workflow |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `orchestrator` | `iaas.capabilities.Orchestrated` |   | `iaas.relationships.abstract.Orchestrates` | [0, UNBOUNDED] |
