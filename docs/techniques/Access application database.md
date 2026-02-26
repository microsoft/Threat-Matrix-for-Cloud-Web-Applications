---
hide:
  - toc
  - footer
---

# Access application database

!!! info inline end
    ID: MS-TA7025<br>
    Tactic: [Collection](../tactics/Collection/index.md)<br>
    MITRE technique: [T1213](https://attack.mitre.org/techniques/T1213/)

Many applications rely on a connected database to store application data, user information, configuration values, or state. The application often connects to the database by using the application cloud identity, or by using a hardcoded connection string. If an attacker gains code execution abilities, they can interact with the database - query and extract data or modify entries. In cases where the database is accessible from the internet, attacker may only need read permissions over the web app to access the database.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Grant applications and identities only the database permissions required for their function.|
|[MS-M7013](../mitigations/Restrict%20network%20access%20to%20sensitive%20services.md)|Restrict network access to sensitive services|Use private endpoints, VPC/VNET integration, or firewall rules to prevent direct internet access to databases.|
|[MS-M7038](../mitigations/Use%20parameterized%20queries.md)|Use parameterized queries|Implement prepared statements and parameterized queries to prevent SQL injection and unauthorized query manipulation.|
