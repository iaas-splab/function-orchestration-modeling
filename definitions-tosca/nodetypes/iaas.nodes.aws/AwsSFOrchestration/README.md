![](https://img.shields.io/badge/Status:-RELEASED-green)

## AwsSFOrchestration Node Type

Node type representing a serverless function orchestration for AWS Step Functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsSFOrchestration` | `iaas.nodes.aws.AwsSFOrchestration` | 1.0.0 | `iaas.nodes.abstract.Workflow` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `state_machine` | `true` | `string` |   |   | the Amazon States Language definition of the state machine |
| `schedule_expression` | `false` | `string` | | | A cron or rate expression to define a CloudWatch rule for scheduled triggering of the function orchestration |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `orchestrator` | `iaas.capabilities.Orchestrated` |   | `iaas.relationships.aws.AwsSFOrchestrates` | [0, UNBOUNDED] |


### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `role_arn`
    * `state_machine`
    * `schedule_expression`