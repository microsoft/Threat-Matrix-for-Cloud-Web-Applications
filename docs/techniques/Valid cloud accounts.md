---
hide:
  - toc
  - footer
---

# Valid cloud accounts

!!! info inline end
    ID: MS-TA7008<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md), [Persistence](../tactics/Persistence/index.md)<br>
    MITRE technique: [T1078.004](https://attack.mitre.org/techniques/T1078/004/)

Adversaries may gain access to cloud web applications and serverless environments by leveraging compromised valid cloud accounts. Using legitimate credentials allows attackers to interact with such services without raising suspicion. This enables them to deploy or modify application code, configure triggers, and maintain control over workloads.

For example, if an attacker gains control over an Entra ID user with owner permissions over a subscription, they would be able to read and modify any function that reside in the subscription. 

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7012](../mitigations/Enforce%20multi-factor%20authentication%20(MFA).md)|Enforce multi-factor authentication (MFA)|Require MFA for all user and administrative accounts to prevent unauthorized access from stolen credentials.|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Grant users and service accounts only the minimum permissions required for their role.|
|[MS-M7018](../mitigations/Use%20conditional%20access%20policies.md)|Use conditional access policies|Restrict account access based on contextual factors such as IP address, device compliance, risk level, or time of day.|
