![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureClientFunction Node Type

A node type that represents a client function on Azure Durable Functions. This function is required to trigger the OrchestratingFunction.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureClientFunction` | `iaas.nodes.azure.durablefunctions.AzureClientFunction` | 1.0.0 | `iaas.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `zip_file` | `true` | `string` |   |  | The file path of code to execute (and function.json for certain languages) |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzureFunctionApp` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `code_path`

