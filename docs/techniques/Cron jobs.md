---
hide:
  - toc
  - footer
---

# Cron jobs

!!! info inline end
    ID: MS-TA7013<br>
    Tactic: [Persistence](../tactics/Persistence/index.md)<br>
    MITRE technique: [T1053](https://attack.mitre.org/techniques/T1053/)

In cases where a cloud application uses scheduled or trigger-based tasks, an attacker with the ability to create or modify such jobs can cause their malicious code to execute automatically. Because these jobs can run independently of normal request flows and often inherit the application's privileges, control over a scheduled or event-triggered job allows persistent execution even if the main application code is updated.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Restrict who can create or modify scheduled jobs.|
