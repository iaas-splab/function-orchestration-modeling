![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## IbmObjectStorageBucket Node Type

A node type that represents an IBM Cloud Object Storage Bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `IbmObjectStorageBucket` | `iaas.nodes.ibm.IbmObjectStorageBucket` | 1.0.0 | `iaas.nodes.abstract.ObjectStorage` |


### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.ibm.IbmPlatform` | `tosca.relationships.HostedOn`| [1, 1] |
| `invoker` | `iaas.capabilities.Invocable` | `iaas.nodes.ibm.IbmCloudFunction` | `iaas.relationships.ibm.IbmCOSTriggers`| [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`