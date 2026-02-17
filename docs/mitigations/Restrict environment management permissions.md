---
hide:
  - toc
  - footer
---

# Restrict Environment Management Permissions

!!! info inline end
    ID: MS-M7021<br>
    MITRE mitigation: -

Limit RBAC permissions to prevent unauthorized creation, modification, or swapping of deployment slots, staging environments, or alternate versions. This prevents attackers from using non-production environments to deploy malicious code.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7011](../techniques/Development%20slots.md)|Development slots|Limit RBAC permissions to prevent unauthorized creation, modification, or swapping of deployment slots.|
