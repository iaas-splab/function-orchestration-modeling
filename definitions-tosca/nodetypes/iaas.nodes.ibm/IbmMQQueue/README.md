![](https://img.shields.io/badge/Status:-RELEASED-green)

## IbmMQQueue Node Type

Ibm-cpsecific node type representing a message queue created on IBM MQ Cloud.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `IbmMQQueue` | `iaas.nodes.ibm.IbmMQQueue` | 1.0.0 | `iaas.nodes.abstract.Queue` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.ibm.IbmPlatform` | `tosca.relationships.HostedOn` | [1, 1] |