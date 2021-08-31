![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AzureStorageQueue Node Type

A node type that represents a message queue on Azure Storage Queue service.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureStorageQueue` | `iaas.nodes.azure.AzureStorageQueue` | 1.0.0 | `iaas.nodes.abstract.Queue` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn`| [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `queue_name`
