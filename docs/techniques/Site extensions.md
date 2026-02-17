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

Site extensions are an Azure App Services feature that allows users to install additional tools onto the web application. Installing unfamiliar extensions could result in malicious code running in the web app.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7023](../mitigations/Install%20trusted%20extensions%20only.md)|Install trusted extensions only|Define and enforce a list of approved extensions that can be installed on App Service instances.|
