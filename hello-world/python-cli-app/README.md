# Simple Python CLI App - OCI Python SDK Sample

[![License: UPL](https://img.shields.io/badge/license-UPL-green)](https://img.shields.io/badge/license-UPL-green) [![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=oracle-devrel_oci-sdk-java-samples)](https://sonarcloud.io/dashboard?id=oracle-devrel_oci-sdk-java-samples)

## Introduction
Software Development Kits (SDKs) Build and deploy apps that integrate with Oracle Cloud Infrastructure services. Each SDK provides the tools you need to develop an app, including code samples and documentation to create, test, and troubleshoot. In addition, if you want to contribute to the development of the SDKs, they are all open source and available on GitHub.

This project sample helps developers to setup their first OCI SDK based python application.

## Cloning this Sample
If you have your OCI tenancy and want to try out this sample, click on 'Open in Code Editor' button below to clone this repository in your cloud shell workspace.

[<img src="https://raw.githubusercontent.com/oracle-devrel/oci-code-editor-samples/main/images/open-in-code-editor.png" />](https://cloud.oracle.com/?region=home&cs_repo_url=https://github.com/oracle-devrel/oci-sdk-python-samples.git&cs_open_ce=true&cs_readme_path=hello-world/python-cli-app/README.md)

or

```
git init python-cli-app
cd python-cli-app
git remote add origin https://github.com/oracle-devrel/oci-sdk-python-samples.git
git config core.sparsecheckout true
echo "hello-world/python-cli-app/*">>.git/info/sparse-checkout
git pull --depth=1 origin main
cd hello-world/python-cli-app/
```

## Installation

You need install the pre-requirements for run this example.

Update repositories of available packages to install, with the following command:

```
$ sudo apt update
```

Install necessary minimum dependencies, with the following command:

```
$ sudo apt install python3-dev python3-pip python3-virtualenv sqlitebrowser
```

For run this example need to install Django framework execute the follow command:

```
$ sudo pip install -r requirements.txt
```

## Running the Program

```
python3 list-instance.py
```
This will print all the instances from the root tenancy in `US-ASHBURN-1` region. The tenancy info is retrieved from OCI config.

## References
* [Blog - Getting started with OCI Python SDK](https://blogs.oracle.com/linux/post/getting-started-with-the-oracle-cloud-infrastructure-python-sdk)
* [OCI SDK - Official Documentation](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm)
* [OCI Python SDK - Open Source GitHub Repository](https://github.com/oracle/oci-python-sdk)

## Contributors
* Author: Ashok Raja CM
* Collaborators: NA
* Last Review: Aug 2022

## Contributing
This project is open source.  Please submit your contributions by forking this repository and submitting a pull request!  Oracle appreciates any contributions that are made by the open source community.

## License
Copyright (c) 2022 Oracle and/or its affiliates.

Licensed under the Universal Permissive License (UPL), Version 1.0.

See [LICENSE](../../LICENSE) for more details.

ORACLE AND ITS AFFILIATES DO NOT PROVIDE ANY WARRANTY WHATSOEVER, EXPRESS OR IMPLIED, FOR ANY SOFTWARE, MATERIAL OR CONTENT OF ANY KIND CONTAINED OR PRODUCED WITHIN THIS REPOSITORY, AND IN PARTICULAR SPECIFICALLY DISCLAIM ANY AND ALL IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.  FURTHERMORE, ORACLE AND ITS AFFILIATES DO NOT REPRESENT THAT ANY CUSTOMARY SECURITY REVIEW HAS BEEN PERFORMED WITH RESPECT TO ANY SOFTWARE, MATERIAL OR CONTENT CONTAINED OR PRODUCED WITHIN THIS REPOSITORY. IN ADDITION, AND WITHOUT LIMITING THE FOREGOING, THIRD PARTIES MAY HAVE POSTED SOFTWARE, MATERIAL OR CONTENT TO THIS REPOSITORY WITHOUT ANY REVIEW. USE AT YOUR OWN RISK. 