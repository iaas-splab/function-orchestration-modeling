![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AwsPlatform  Node Type

A node type that represents the AWS platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsPlatform` | `iaas.nodes.aws.AwsPlatform` | 1.0.0 | `iaas.nodes.abstract.CloudPlatform` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `role_arn` | `string` |   | AWS role arn identifier |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |  | AWS |  |
| `region` | `true` | `string` |  |  | The region identifier, e.g., us-west-1 |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[ iaas.nodes.aws.AwsLambdaFunction, iaas.nodes.aws.AwsS3Bucket, iaas.nodes.aws.AwsSFOrchestration, iaas.nodes.aws.AwsSQSQueue ]` | [1, UNBOUNDED] |
