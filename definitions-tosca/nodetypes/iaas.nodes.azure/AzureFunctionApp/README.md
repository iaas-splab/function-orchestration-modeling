![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureFunctionApp Node Type

A node type that represents an Azure Function App that groups one or more Azure Functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureFunctionApp` | `iaas.nodes.azure.AzureFunctionApp` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | The name of the function app |
| `host_file` | `true` | `string` |   |   | The path to runtime-specific configurations of the function app |
| `dependencies_zip` | `false` | `list` |   |   | The list of paths to dependencies (files or archived folders containing shared libraries) required for the function app |


### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `host_file`
    * `dependencies`
