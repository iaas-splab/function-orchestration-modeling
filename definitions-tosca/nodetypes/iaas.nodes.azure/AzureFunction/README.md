![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureFunction Node Type

A node type that represents a function on Azure Functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureFunction` | `iaas.nodes.azure.AzureFunction` | 1.0.0 | `iaas.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `zip_file` | `true` | `string` |   |  | The file path of code to execute (and function.json for certain languages) |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Capabilities

| Name | Capability Type | Valid Source Types | Occurrences |
|:---- |:--------------- |:-------------------- |:------------|
| `grouped` | `iaas.capabilities.Grouped` | `[ iaas.nodes.azure.AzureFunctionApp ]` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `code_path`

