# Standards-based Modeling and Deployment of Function Orchestrations 
This project comprises a hierarchy of TOSCA types for modeling the deployment of serverless function orchestrations both independently and combined with event-driven serverless components.

## Project Structure
This project contains the following folders:
1. **definitions-tosca**:
This folder comprises the TOSCA types hierarchy which enables modeling the deployment of serverless function orchestrations.
The repository format is compatible with [Eclipse Winery](https://github.com/eclipse/winery), hence, it can be imported as a Winery repository for graphical deployment modeling.
Furthermore, the deployment logic is implemented using Ansible to enable deploying resulting TOSCA models with [xOpera](https://github.com/xlab-si/xopera-opera), an open source TOSCA deployment automation technology.
2. **etl-case-study**:
This folder comprises code artifacts implementing a case study showcasing the usage of BPMN and TOSCA for modeling serverless function orchestrations and their automated deployment.
The function orchestration used for the case study is an extract-transform-load pipeline for processing the Open Air Quality data.
This ETL function orchestration is combined with several standalone serverless components in an example serverless application that combines event-driven behavior with a function orchestration.