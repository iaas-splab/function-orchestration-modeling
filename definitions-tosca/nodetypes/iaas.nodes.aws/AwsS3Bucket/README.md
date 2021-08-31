![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AwsS3Bucket Node Type

A node type that represents an AWS S3 Bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsS3Bucket` | `iaas.nodes.aws.AwsS3Bucket` | 1.0.0 | `iaas.nodes.abstract.ObjectStorage` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `region` | `string` |   | Region value |
| `bucket_url_path` | `string` |  | URL of the bucket using path-style access (https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html) |
| `bucket_url_vhost` | `string` |  | URL of the bucket using virtual-hosted-style access (https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html) |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn`| [1, 1] |
| `invoker` | `iaas.capabilities.Invocable` | `iaas.nodes.aws.AwsLambdaFunction` | `iaas.relationships.aws.AwsS3Triggers`| [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_region`
    * `bucket_name`
