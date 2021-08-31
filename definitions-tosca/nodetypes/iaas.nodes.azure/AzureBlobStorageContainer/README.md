![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureBlobStorageContainer Node Type

A node type that represents an Azure blob storage container.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureBlobStorageContainer` | `iaas.nodes.azure.AzureBlobStorageContainer` | 1.0.0 | `iaas.nodes.abstract.ObjectStorage` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `resource_group`
    * `storage_account`
