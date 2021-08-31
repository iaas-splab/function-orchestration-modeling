![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AwsSQSQueue Bucket Node Type

A node type that represents an AWS SQS queue.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsSQSQueue` | `iaas.nodes.aws.AwsSQSQueue` | 1.0.0 | `iaas.nodes.abstract.Queue` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon's resource name for this queue |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn`| [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_region`
    * `queue_name`
