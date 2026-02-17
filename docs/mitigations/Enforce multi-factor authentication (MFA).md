---
hide:
  - toc
  - footer
---

# Enforce Multi-Factor Authentication (MFA)

!!! info inline end
    ID: MS-M7012<br>
    MITRE mitigation: [M1032](https://attack.mitre.org/mitigations/M1032/)

Require multi-factor authentication for all user and administrative accounts accessing cloud web applications and management interfaces. MFA adds an additional layer of security beyond passwords, significantly reducing the risk of unauthorized access from compromised credentials.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7008](../techniques/Valid%20cloud%20accounts.md)|Valid cloud accounts|Require MFA for all user and administrative accounts to prevent unauthorized access from stolen credentials.|
|[MS-TA7005](../techniques/Exposed%20misconfigured%20admin%20interfaces.md)|Exposed/misconfigured admin interfaces|Require MFA for access to all administrative and management interfaces.|
|[MS-TA7010](../techniques/Cloud%20native%20terminal.md)|Cloud native terminal|Require MFA for all access to administrative shell and console features.|
|[MS-TA7018](../techniques/Brute%20force.md)|Brute force|Require MFA to prevent credential-based access even if passwords are guessed.|
