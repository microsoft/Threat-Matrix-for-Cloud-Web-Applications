---
hide:
  - toc
  - footer
---

# Restrict Delete and Write Permissions

!!! info inline end
    ID: MS-M7040<br>
    MITRE mitigation: [M1022](https://attack.mitre.org/mitigations/M1022/)

Limit who can delete or modify data in storage accounts, databases, and other repositories. Restricting destructive permissions prevents attackers from causing data loss even if they gain access to the environment.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7027](../techniques/Data%20destruction.md)|Data destruction|Limit who can delete or modify data in storage accounts, databases, and other repositories.|
