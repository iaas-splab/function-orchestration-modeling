# Open Air Quality ETL Function Orchestration Blueprint for IBM
This project contains a deployable TOSCA model of a function orchestration combined with regular serverless components implemented for IBM services.
The details on the implementations are provided [in the case study description](../../../../etl-case-study/README.md).
The TOSCA model of the application created in Eclipse Winery is shown below:
![IBM Model](ibm-app.png)

## How to Deploy it
To deploy this TOSCA model, several requirements need to be fulfilled. 
Firstly, this model relies on the [xOpera TOSCA orchestrator](https://github.com/xlab-si/xopera-opera), since all deployment logic is implemented using Ansible. 
xOpera needs to be [installed](https://xlab-si.github.io/xopera-docs/opera_cli.html#installation) on the machine from which the deployment will be enacted.
The implemented deployment scripts require having the following IBM CLI components installed on the machine where xOpera is launched:
1. [IBM CLI](https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli)
2. [IBM Cloud Object Storage CLI plug-in](https://cloud.ibm.com/docs/cli?topic=cli-install-devtools-manually#installing-ibm-cloud-object-storage-cli-plug-in)
3. [IBM Cloud Functions CLI plug-in](https://cloud.ibm.com/docs/cli?topic=cli-install-devtools-manually#idt-install-functions)
4. [IBM Composer npm package](https://github.com/ibm-functions/composer#installation)

The sign in via IBM CLI is achieved using the API key which needs to be specified as `IC_API_KEY` or `IBMCLOUD_API_KEY` environment variables (IBM CLI checks the presence of these variables).
Further, to enable creating queues on IBM MQ, two additional environment variables need to be specified, namely `IBMMQ_ADMINISTRATIVE_ENDPOINT` with the administrative REST endpoint of the IBM MQ manager, and `IBMMQ_BASIC_AUTH_STRING` with the basic authentication string.
The environment variables can be added for a session as follows:
```
export IC_API_KEY=MY-API-KEY
export IBMCLOUD_API_KEY=MY-API-KEY
export IBMMQ_ADMINISTRATIVE_ENDPOINT=ADMIN-ENDPOINT-FOR-IBM-MQ
export IBMMQ_BASIC_AUTH_STRING=MY-BASIC-AUTH-STRING
```
The basic authentication string can be obtained by issuing the following command:
```
echo "<MQ_USERNAME>:<API_KEY>" | base64
```

Export the CSAR using Eclipse Winery and execute 
```
opera deploy <csar root directory>
```
For more information on export of CSARs, see Eclipse Winery's [documentation](https://winery.readthedocs.io/en/latest/user/getting-started.html).


## Additional Dependencies
To enable running parallel compositions in IBM Composer requires accessing a Redis instance, which can be provisioned, e.g., using IBM Databases for Redis service.
More information about this requirement can be found [in IBM Composer documentation](https://github.com/ibm-functions/composer#parallel-compositions-with-redis).
The configuration of such Redis instance can be done as [explained here](https://github.com/iaas-splab/faas-migration/tree/master/MatrixMultiplication/IBMCloud).
It is important to create service credentials and provide the connection data exactly from this service credentials, and not simply using the endpoint connection data.
The redis connectivity information is specified in the ServiceTemplate.tosca as the `ETLparams` artifact attached to the `IbmComposerOrchestration_0` Node Template.
ETLparams.json has the following structure:
```
{
  "$composer": {
    "redis": {
      "uri": "rediss://admin:pwd@xxx.databases.appdomain.cloud:32495/0",
      "ca": "myCert"
    }
  }
}
```
