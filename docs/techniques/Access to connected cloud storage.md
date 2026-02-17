---
hide:
  - toc
  - footer
---

# Access to connected cloud storage

!!! info inline end
    ID: MS-TA7020<br>
    Tactic: [Discovery](../tactics/Discovery/index.md)<br>
    MITRE technique: 

Cloud applications often use external storage services for hosting source code, configuration files or assets. Attackers may exploit misconfigured or compromised read access to this storage to review the code and configuration to find vulnerabilities or sensitive information that could be exploited to take over the application.

For example, in GCP Cloud Run functions, the function code is saved into a bucket in the project. If an attacker compromised a user with storage read access, they would be able to view the source code.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Grant applications and users only the minimum necessary permissions to storage resources.|
|[MS-M7013](../mitigations/Restrict%20network%20access%20to%20sensitive%20services.md)|Restrict network access to sensitive services|Use private endpoints, VPC/VNET integration, or firewall rules to limit storage access to authorized networks.|
