![](https://img.shields.io/badge/Status:-RELEASED-green)

## Cloud Platform Node Type (Abstract)

Abstract node type representing a provider-managed cloud platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `CloudPlatform` | `iaas.nodes.abstract.CloudPlatform` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the cloud platform |

### Capabilities
| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` |  | [1, UNBOUNDED] |
