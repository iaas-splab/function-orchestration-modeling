![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzurePlatform Node Type

A node type that represents a set of configurations for Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzurePlatform` | `iaas.nodes.azure.AzurePlatform` | 1.0.0 | `iaas.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |  | IBM |  |
| `region` | `true` | `string` |  |  | The region identifier, e.g., us-west-1 |


### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[ iaas.nodes.azure.AzureFunctionApp, iaas.nodes.azure.AzureBlobStorageContainer, iaas.nodes.azure.AzureStorageQueue ]` | [1, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `region`
    * `resource_group`
    * `cos_crn`