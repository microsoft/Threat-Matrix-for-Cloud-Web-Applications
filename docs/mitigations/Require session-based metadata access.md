---
hide:
  - toc
  - footer
---

# Require Session-Based Metadata Access

!!! info inline end
    ID: MS-M7028<br>
    MITRE mitigation: -

Use IMDSv2 (AWS) or equivalent protections that require token-based sessions to access metadata APIs. Session-based access adds an additional layer of protection against unauthorized metadata queries.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7016](../techniques/Access%20workload%20identity%20credentials.md)|Access workload identity credentials|Use IMDSv2 (AWS) or equivalent protections that require token-based sessions to access metadata APIs.|
