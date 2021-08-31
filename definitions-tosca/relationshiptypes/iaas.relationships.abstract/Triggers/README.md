## Triggers Relationship (Abstract)

Abstract relationship type representing triggering of an invocable node.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Triggers` | `iaas.relationships.abstract.Triggers` | 1.0.0 | `tosca.relationships.ConnectsTo` |

### Valid Target types

* `iaas.capabilities.Invocable`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `false` | `list` |   |   | List of events |