---
hide:
  - toc
  - footer
---

# Event data capture

!!! info inline end
    ID: MS-TA7026<br>
    Tactic: [Collection](../tactics/Collection/index.md)<br>
    MITRE technique: [T1213](https://attack.mitre.org/techniques/T1213/)

Cloud applications often generate logs that include diagnostic data, request metadata, or user input. These logs may be stored locally, streamed to external services, or accessed via debugging interfaces. If an attacker gains access to the application or its logging infrastructure, they may collect sensitive information that aids further exploitation or reconnaissance.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Restrict permissions to read logs and diagnostic data to only authorized users and roles.|
|[MS-M7011](../mitigations/Disable%20basic%20authentication.md)|Disable basic authentication|Turn off basic authentication for log streaming endpoints and diagnostic interfaces.|
|[MS-M7039](../mitigations/Avoid%20logging%20sensitive%20data.md)|Avoid logging sensitive data|Configure logging filters to exclude passwords, API keys, tokens, and PII from application logs.|
