---
hide:
  - toc
  - footer
---

# Access cloud resources

!!! info inline end
    ID: MS-TA7015<br>
    Tactic: [Privilege Escalation](../tactics/PrivilegeEscalation/index.md), [Lateral Movement](../tactics/LateralMovement/index.md)<br>
    MITRE technique: [T1078.004](https://attack.mitre.org/techniques/T1078/004/)

Web apps deployed in the cloud often run with identities or service accounts that have permissions over additional cloud resources in the environment such as storage, databases and AI services. Additionally, some applications store connection strings or keys to cloud resources in the app configuration files or environment variables. Therefore, if attackers compromise the application, they can often extract or leverage these credentials to access additional cloud resources.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Scope identity permissions tightly to specific resources and actions using resource-level policies and deny-by-default strategies.|
|[MS-M7026](../mitigations/Use%20workload%20identities%20instead%20of%20static%20credentials.md)|Use workload identities instead of static credentials|Avoid storing connection strings or access keys in application configuration. Use workload identities for resource access.|
