---
hide:
  - toc
  - footer
---

# Site extensions

!!! info inline end
    ID: MS-TA7012<br>
    Tactic: [Execution](../tactics/Execution/index.md)<br>
    MITRE technique: 

Site extensions are an Azure App Services feature that allows users to install additional tools and utilities onto their web application. These extensions run within the context of the App Service and have the same permissions as the application itself - including requests data, file system access and environment variables.
The extensions are installed from a public NuGet-based feed, to which anyone can upload to. If an attacker publishes a malicious extension with a name similar to a legitimate one (typosquatting) or compromises an existing extension package, unsuspecting users may install it, causing malicious code to run in their application.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7023](../mitigations/Install%20trusted%20extensions%20only.md)|Install trusted extensions only|Define and enforce a list of approved extensions that can be installed on App Service instances.|
