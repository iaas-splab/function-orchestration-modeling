![](https://img.shields.io/badge/Status:-RELEASED-green)

## IbmComposerOrchestration Node Type

Abstract node type representing a serverless workflow independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `IbmComposerOrchestration` | `iaas.nodes.ibm.IbmComposerOrchestration` | 1.0.0 | `iaas.nodes.abstract.Workflow` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the orchestrating function |
| `workflow` | `true` | `string` |   |   | The workflow definition in JavaScript |
| `timeout` | `true` | `string` |   | `900000` | The timeout limit to terminate the action, specified in milliseconds |
| `memory` | `true` | `string` |   | `256` | The maximum memory for the action, specified in MBs |
| `runtime` | `true` | `string` |   | `nodejs:12` | Orchestrating function's runtime, currently only JavaScript is considered |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.ibm.IbmPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `orchestrator` | `iaas.capabilities.Orchestrated` |   | `iaas.relationships.ibm.IbmComposerOrchestrates` | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `workflow`
    * `timeout`
    * `memory`
    * `runtime`