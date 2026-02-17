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

Cloud-based application code is often loaded from a git repository, cloud storage or external registries. If an attacker can modify this code, they may deploy changes that will run every time the application is restarting or handling a request, possibly blending with the normal behavior of the application.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7024](../mitigations/Restrict%20write%20access%20to%20code%20repositories.md)|Restrict write access to code repositories|Limit who can push to production branches and require protected branch policies.|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Protect build and deployment workflows from unauthorized changes with access controls and approval gates.|
|[MS-M7025](../mitigations/Require%20signed%20commits.md)|Require signed commits|Enforce commit signing to verify the authenticity of code changes.|
