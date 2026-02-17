---
hide:
  - toc
  - footer
---

# Centralize Logs to Protected Accounts

!!! info inline end
    ID: MS-M7030<br>
    MITRE mitigation: [M1029](https://attack.mitre.org/mitigations/M1029/)

Send logs to separate, restricted accounts or projects where application identities cannot modify or delete them. Centralizing logs to protected destinations ensures attackers cannot tamper with audit trails even if they compromise the application.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7017](../techniques/Disable%20cloud%20logging.md)|Disable cloud logging|Send logs to separate, restricted accounts or projects where application identities cannot modify or delete them.|
