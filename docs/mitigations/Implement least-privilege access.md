---
hide:
  - toc
  - footer
---

# Implement Least-Privilege Access

!!! info inline end
    ID: MS-M7017<br>
    MITRE mitigation: [M1026](https://attack.mitre.org/mitigations/M1026/)

Grant users, service accounts, and applications only the minimum permissions necessary to perform their intended functions. This limits the potential impact of compromised accounts or applications by restricting what actions an attacker can take.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7008](../techniques/Valid%20cloud%20accounts.md)|Valid cloud accounts|Grant users and service accounts only the minimum permissions required for their role.|
|[MS-TA7020](../techniques/Access%20to%20connected%20cloud%20storage.md)|Access to connected cloud storage|Grant applications and users only the minimum necessary permissions to storage resources.|
|[MS-TA7006](../techniques/Serverless%20trigger%20injection.md)|Serverless trigger injection|Grant serverless functions only the permissions necessary to complete their tasks.|
|[MS-TA7010](../techniques/Cloud%20native%20terminal.md)|Cloud native terminal|Restrict permissions to access cloud-native terminals (Kudu, Systems Manager, Cloud Shell) to only authorized administrators.|
|[MS-TA7013](../techniques/Cron%20jobs.md)|Cron jobs|Restrict who can create or modify scheduled jobs.|
|[MS-TA7023](../techniques/Connector%20reuse.md)|Connector reuse|Restrict who can view or modify connector configurations containing third-party credentials.|
|[MS-TA7026](../techniques/Event%20data%20capture.md)|Event data capture|Restrict permissions to read logs and diagnostic data to only authorized users and roles.|
|[MS-TA7025](../techniques/Access%20application%20database.md)|Access application database|Grant applications and identities only the database permissions required for their function.|
|[MS-TA7028](../techniques/Data%20theft.md)|Data theft|Limit access to sensitive data based on need-to-know principles and role-based permissions.|
|[MS-TA7016](../techniques/Access%20workload%20identity%20credentials.md)|Access workload identity credentials|Grant workload identities (managed identities, IAM roles, or service accounts) only the minimum permissions needed for their function.|
|[MS-TA7015](../techniques/Access%20cloud%20resources.md)|Access cloud resources|Scope identity permissions tightly to specific resources and actions using resource-level policies and deny-by-default strategies.|
