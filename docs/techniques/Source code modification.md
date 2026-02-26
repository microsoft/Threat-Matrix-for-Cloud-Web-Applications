---
hide:
  - toc
  - footer
---

# Source code modification

!!! info inline end
    ID: MS-TA7014<br>
    Tactic: [Persistence](../tactics/Persistence/index.md)<br>
    MITRE technique: 

An attacker with access to a development environment may be able to modify the application's source - which could reside in a git repository, a container image in a registry, or a deployment package in cloud storage. Because cloud web applications are typically deployed through automated pipelines, a single modification can propagate automatically into production, causing the attacker's code to run every time the application restarts. These changes become part of the application's canonical source, meaning that even if the runtime environment is rebuilt or scaled, the tainted code is redeployed from the same trusted source, maintaining the attacker's access to the application.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7024](../mitigations/Restrict%20write%20access%20to%20code%20repositories.md)|Restrict write access to code repositories|Limit who can push to production branches and require protected branch policies.|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Protect build and deployment workflows from unauthorized changes with access controls and approval gates.|
|[MS-M7025](../mitigations/Require%20signed%20commits.md)|Require signed commits|Enforce commit signing to verify the authenticity of code changes.|