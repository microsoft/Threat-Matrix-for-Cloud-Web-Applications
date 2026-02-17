---
hide:
  - toc
  - footer
---

# Resource hijacking

!!! info inline end
    ID: MS-TA7031<br>
    Tactic: [Impact](../tactics/Impact/index.md)<br>
    MITRE technique: [T1496](https://attack.mitre.org/techniques/T1496/)

Attackers may leverage the compute, network, or storage resources of the application for unauthorized purposes, such as cryptocurrency mining, mass scanning, or traffic proxying.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7037](../mitigations/Restrict%20outbound%20network%20access.md)|Restrict outbound network access|Limit outbound traffic from applications and functions to explicitly approved domains or IP ranges to prevent misuse.|
|[MS-M7045](../mitigations/Use%20compute%20reservations.md)|Use compute reservations|Limit scaling behavior with autoscaling limits.|
|[MS-M7044](../mitigations/Implement%20resource%20quotas%20and%20concurrency%20limits.md)|Implement resource quotas and concurrency limits|Set maximum CPU, memory, execution time, and concurrency limits on serverless functions and applications.|
