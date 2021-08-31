## AwsS3Triggers Relationship

AWS-specific relationship type representing AwsS3-to-AwsLambdaFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsS3Triggers` | `iaas.relationships.aws.AwsS3Triggers` | 1.0.0 | `iaas.relationships.abstract.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `true` | `string` |   |   | List of events |
