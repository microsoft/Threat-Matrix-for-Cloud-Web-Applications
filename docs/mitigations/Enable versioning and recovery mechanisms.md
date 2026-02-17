---
hide:
  - toc
  - footer
---

# Enable Versioning and Recovery Mechanisms

!!! info inline end
    ID: MS-M7034<br>
    MITRE mitigation: [M1053](https://attack.mitre.org/mitigations/M1053/)

Use version control and automated rollback capabilities to quickly restore legitimate content after unauthorized modifications. Versioning enables rapid recovery from defacement or other malicious changes.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7029](../techniques/Defacement.md)|Defacement|Use version control and automated rollback capabilities to quickly restore legitimate content.|
|[MS-TA7027](../techniques/Data%20destruction.md)|Data destruction|Use versioning, soft delete, or recycle bins to allow recovery of deleted or modified data.|
