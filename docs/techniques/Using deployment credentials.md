---
hide:
  - toc
  - footer
---

# Using deployment credentials

!!! info inline end
    ID: MS-TA7007<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md)<br>
    MITRE technique: 

In some cloud web applications, deployment credentials can grant management access beyond publishing new code. Adversaries who obtain such credentials might be able to use them to directly interact with the application without modifying its source code.

For example, in Azure App Service, the FTPS credential can be used to access the SCM (source control management) console, which allows connecting to the application over ssh, thus allowing attacker full control over the app. If the compromised credentials are User-scope, they can be used for all applications the user has contributor permissions over.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7018](../mitigations/Use%20conditional%20access%20policies.md)|Use conditional access policies|Restrict account access based on contextual factors such as IP address, device compliance, risk level, or time of day.|
|[MS-M7019](../mitigations/Enforce%20credential%20rotation%20policies.md)|Enforce credential rotation policies|Regularly rotate deployment credentials such as personal access tokens, publish profiles, and service principal secrets.|
|[MS-M7020](../mitigations/Use%20secrets%20management%20solutions.md)|Use secrets management solutions|Store deployment credentials in dedicated secret managers rather than in code repositories or CI/CD configuration files.|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Restrict access to CI/CD systems, enforce code review for pipeline changes, and use secret scanning tools to prevent credential leaks.|