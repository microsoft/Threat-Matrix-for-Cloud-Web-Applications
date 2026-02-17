---
hide:
  - toc
  - footer
---

# Data theft

!!! info inline end
    ID: MS-TA7028<br>
    Tactic: [Impact](../tactics/Impact/index.md)<br>
    MITRE technique: 

If attackers gain access to the application, its storage, or connected cloud resources, they may retrieve data stored or processed by the application. This includes application content, user information, configuration files, or proprietary content.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Limit access to sensitive data based on need-to-know principles and role-based permissions.|
|[MS-M7037](../mitigations/Restrict%20outbound%20network%20access.md)|Restrict outbound network access|Use egress filtering and firewall rules to prevent unauthorized data exfiltration.|
