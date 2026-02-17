---
hide:
  - toc
  - footer
---

# Use Parameterized Queries

!!! info inline end
    ID: MS-M7038<br>
    MITRE mitigation: [M1013](https://attack.mitre.org/mitigations/M1013/)

Implement prepared statements and parameterized queries when interacting with databases. Parameterized queries prevent SQL injection attacks by separating code from data, ensuring user input cannot modify query structure.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7025](../techniques/Access%20application%20database.md)|Access application database|Implement prepared statements and parameterized queries to prevent SQL injection and unauthorized query manipulation.|
