![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureOrchestratingFunction Node Type

A node type that represents an orcchestrating function for Azure Durable Functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureOrchestratingFunction` | `iaas.nodes.azure.durablefunctions.AzureOrchestratingFunction` | 1.0.0 | `iaas.nodes.abstract.Workflow` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `zip_file` | `true` | `string` |   |  | The file path of code to execute (and function.json for certain languages) |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzureFunctionApp` | `tosca.relationships.HostedOn` | [1, 1] |
| `orchestrator` | `iaas.capabilities.Orchestrated` | `iaas.nodes.azure.durablefunctions.AzureActivityFunction` | `iaas.relationships.azure.AzureDFOrchestrates` | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `code_path`