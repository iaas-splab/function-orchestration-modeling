![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## IbmCloudFunction Node Type

A node type that represents an IBM Cloud Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `IbmCloudFunction` | `iaas.nodes.ibm.IbmCloudFunction` | 1.0.0 | `iaas.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `namespace` | `true` | `string` |   |   | The name of the function namespace |
| `timeout` | `true` | `integer` |   | 60000 | The timeout limit to terminate the action, specified in milliseconds |
| `memory` | `true` | `integer` |   | 256 | The maximum memory for the action, specified in MBs |
| `runtime` | `true` | `string` |   | `python:3.7` | Function runtime (List of possible values - https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-runtimes) |
| `handler` | `true` | `string` |   | `main` | Handler for cloud function |
| `zip_file` | `true` | `string` |   |  | The file path of code to execute and it supports only .zip extension to create the action |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `iaas.nodes.ibm.IbmPlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `name`
    * `namespace`
    * `timeout`
    * `memory`
    * `runtime`
    * `handler`
    * `code_path`