---
hide:
  - toc
  - footer
---

# Use Workload Identities Instead of Static Credentials

!!! info inline end
    ID: MS-M7026<br>
    MITRE mitigation: [M1026](https://attack.mitre.org/mitigations/M1026/)

Use platform-provided workload identities for resource access instead of storing connection strings, access keys, or other static credentials in application configuration. Workload identities eliminate the need to manage and rotate secrets manually.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7015](../techniques/Access%20cloud%20resources.md)|Access cloud resources|Avoid storing connection strings or access keys in application configuration. Use workload identities for resource access.|
|[MS-TA7019](../techniques/Cloud%20credentials%20in%20runtime%20environment.md)|Cloud credentials in runtime environment|Avoid storing cloud credentials directly in environment variables or configuration files.|