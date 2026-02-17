---
hide:
  - toc
  - footer
---

# Secure CI/CD Pipelines

!!! info inline end
    ID: MS-M7008<br>
    MITRE mitigation: [M1045](https://attack.mitre.org/mitigations/M1045/)

Protect continuous integration and continuous deployment pipelines with access controls, branch protection rules, mandatory code reviews, and secret scanning. Secure pipelines prevent unauthorized code from being deployed to production environments.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7007](../techniques/Using%20deployment%20credentials.md)|Using deployment credentials|Restrict access to CI/CD systems, enforce code review for pipeline changes, and use secret scanning tools to prevent credential leaks.|
|[MS-TA7003](../techniques/Code%20injection%20in%20connected%20repository.md)|Code injection in connected repository|Protect build and deployment systems with access controls, branch protection, and mandatory code review requirements.|
|[MS-TA7014](../techniques/Source%20code%20modification.md)|Source code modification|Protect build and deployment workflows from unauthorized changes with access controls and approval gates.|
|[MS-TA7029](../techniques/Defacement.md)|Defacement|Protect deployment workflows from unauthorized modifications that could alter application content.|
|[MS-TA7004](../techniques/Compromised%20image%20in%20registry.md)|Compromised image in registry|Placing gates in the CI/CD process can block pushing unsecured code to container images.|
