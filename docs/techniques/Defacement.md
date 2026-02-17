---
hide:
  - toc
  - footer
---

# Defacement

!!! info inline end
    ID: MS-TA7029<br>
    Tactic: [Impact](../tactics/Impact/index.md)<br>
    MITRE technique: [T1491](https://attack.mitre.org/techniques/T1491/)

Adversaries may attempt to alter the web application content or appearance in order to damage reputation, intimidate victims or spread propaganda. This could be done through access to the application itself, to the source code or any assets it uses.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Protect deployment workflows from unauthorized modifications that could alter application content.|
|[MS-M7042](../mitigations/Restrict%20deployment%20permissions.md)|Restrict deployment permissions|Limit who can deploy code or modify application content to authorized personnel only.|
|[MS-M7034](../mitigations/Enable%20versioning%20and%20recovery%20mechanisms.md)|Enable versioning and recovery mechanisms|Use version control and automated rollback capabilities to quickly restore legitimate content.|
