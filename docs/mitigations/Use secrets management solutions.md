---
hide:
  - toc
  - footer
---

# Use Secrets Management Solutions

!!! info inline end
    ID: MS-M7020<br>
    MITRE mitigation: -

Store sensitive credentials, API keys, and connection strings in dedicated secrets management services rather than in code repositories, configuration files, or environment variables. Retrieve secrets dynamically at runtime using identity-based access controls.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7007](../techniques/Using%20deployment%20credentials.md)|Using deployment credentials|Store deployment credentials in dedicated secret managers rather than in code repositories or CI/CD configuration files.|
|[MS-TA7019](../techniques/Cloud%20credentials%20in%20runtime%20environment.md)|Cloud credentials in runtime environment|Store secrets in dedicated secret managers and retrieve them dynamically at runtime using identity-based access.|
