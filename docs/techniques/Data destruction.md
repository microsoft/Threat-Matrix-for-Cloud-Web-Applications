---
hide:
  - toc
  - footer
---

# Data destruction

!!! info inline end
    ID: MS-TA7027<br>
    Tactic: [Impact](../tactics/Impact/index.md)<br>
    MITRE technique: [T1485](https://attack.mitre.org/techniques/T1485/)

Attackers who gain sufficient privileges within a cloud web application may delete or corrupt data stored in the app or in connected cloud resources such as databases and storage.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7040](../mitigations/Restrict%20delete%20and%20write%20permissions.md)|Restrict delete and write permissions|Limit who can delete or modify data in storage accounts, databases, and other repositories.|
|[MS-M7034](../mitigations/Enable%20versioning%20and%20recovery%20mechanisms.md)|Enable versioning and recovery mechanisms|Use versioning, soft delete, or recycle bins to allow recovery of deleted or modified data.|
|[MS-M7041](../mitigations/Implement%20backup%20and%20recovery%20plans.md)|Implement backup and recovery plans|Regularly back up critical data to separate, protected locations and test restoration procedures.|
