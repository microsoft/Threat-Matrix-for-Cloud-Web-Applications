---
hide:
  - toc
  - footer
---

# Disable cloud logging

!!! info inline end
    ID: MS-TA7017<br>
    Tactic: [Defense Evasion](../tactics/DefenseEvasion/index.md)<br>
    MITRE technique: [T1562.008](https://attack.mitre.org/techniques/T1562/008/)

Attackers with appropriate permissions may disable or alter cloud logging to hide their actions and avoid detection.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7029](../mitigations/Restrict%20logging%20configuration%20permissions.md)|Restrict logging configuration permissions|Use policies to prevent unauthorized modification or deletion of logging settings across cloud platforms.|
|[MS-M7030](../mitigations/Centralize%20logs%20to%20protected%20accounts.md)|Centralize logs to protected accounts|Send logs to separate, restricted accounts or projects where application identities cannot modify or delete them.|
