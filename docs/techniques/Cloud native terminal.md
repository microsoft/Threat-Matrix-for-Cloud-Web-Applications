---
hide:
  - toc
  - footer
---

# Cloud native terminal

!!! info inline end
    ID: MS-TA7010<br>
    Tactic: [Execution](../tactics/Execution/index.md)<br>
    MITRE technique: [T1059](https://attack.mitre.org/techniques/T1059/)

Some cloud platforms provide built-in administrative consoles or SSH-style terminals for running commands directly inside the application's execution environment. Attackers who gain access to the terminal will be able to extract data, edit the web app files and execute commands.
For example, Azure App Services expose a Kudu console that acts as a built-in terminal; if attackers obtain deployment credentials, they can use it to browse files, execute commands, and tamper with application code.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Restrict permissions to access cloud-native terminals (Kudu, Systems Manager, Cloud Shell) to only authorized administrators.|
|[MS-M7011](../mitigations/Disable%20basic%20authentication.md)|Disable basic authentication|Turn off username/password authentication where possible.|
|[MS-M7012](../mitigations/Enforce%20multi-factor%20authentication%20(MFA).md)|Enforce multi-factor authentication (MFA)|Require MFA for all access to administrative shell and console features.|
