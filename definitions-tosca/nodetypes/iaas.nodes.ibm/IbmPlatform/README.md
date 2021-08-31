![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## IbmPlatform Node Type

A node type that represents a set of configurations for IBM platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `IbmPlatform` | `iaas.nodes.ibm.IbmPlatform` | 1.0.0 | `iaas.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |  | IBM |  |
| `region` | `true` | `string` |  |  | The region identifier, e.g., us-west-1 |
| `resource_group` | `true` | `string` |  |  | The name of a resource group to target |
| `cos_crn` | `true` | `string` |  |  | CRN of the IBM Cloud Object Storage which will be used |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[ iaas.nodes.ibm.IbmCloudFunction, iaas.nodes.ibm.IbmObjectStorageBucket, iaas.nodes.ibm.IbmComposerOrchestration, iaas.nodes.ibm.IbmMQQueue ]` | [1, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `region`
    * `resource_group`
    * `cos_crn`