---
hide:
  - toc
  - footer
---

# Code injection in connected repository

!!! info inline end
    ID: MS-TA7003<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md)<br>
    MITRE technique: [T1195.002](https://attack.mitre.org/techniques/T1195/002/)

Attackers may inject malicious code into source repositories that are linked to cloud web applications or serverless functions. If these repositories are automatically synced with production environments, the injected code executes under the legitimate workflows.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Protect build and deployment systems with access controls, branch protection, and mandatory code review requirements.|
|[MS-M7009](../mitigations/Enforce%20code%20review%20and%20approval%20workflows.md)|Enforce code review and approval workflows|Require peer review and approval before merging code changes to production branches.|
