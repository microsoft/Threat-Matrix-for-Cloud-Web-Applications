---
hide:
  - toc
  - footer
---

# Restrict Access to Configuration Endpoints

!!! info inline end
    ID: MS-M7033<br>
    MITRE mitigation: -

Disable or secure application configuration endpoints that expose environment variables, settings, or other sensitive configuration data. Restricting access prevents attackers from discovering credentials stored in configuration.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7019](../techniques/Cloud%20credentials%20in%20runtime%20environment.md)|Cloud credentials in runtime environment|Disable or secure application configuration endpoints that expose environment variables or settings.|
