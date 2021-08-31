# TOSCA Definitions for Modeling Function Orchestrations
This repository comprises TOSCA definitions which enable modeling serverless function orchestrations for AWS, Azure, and IBM clouds.
All technology-specific types are derived from the corresponding abstract types, which also enable modeling function orchestrations conceptually.
The format of repository is compatible with Eclipse Winery, hence this repository can be taken as-is for graphical modeling.
Further, the implementation artifacts are created in Ansible, making it possible to automatically deploy the models using xOpera.
The abstract types and some AWS-specific types are based on the [RADON Particles repository](https://github.com/radon-h2020/radon-particles) (see [NOTICE](NOTICE)).
