---
hide:
  - toc
  - footer
---

# Development slots

!!! info inline end
    ID: MS-TA7011<br>
    Tactic: [Execution](../tactics/Execution/index.md), [Defense Evasion](../tactics/DefenseEvasion/index.md)<br>
    MITRE technique: 

Many cloud platforms and serverless environments support staging or preview environments (such as deployment slots in Azure App Services, aliases in AWS Lambda, or revision tags in GCP Cloud Run), which allow developers to test and stage new versions of their applications before swapping them into production. These environments can be swapped or promoted with minimal downtime. If an attacker gains the ability to modify or promote a non-production environment, they may execute malicious code or gain insights into the application's structure and behavior.
In some cases, these staged environments are directly accessible without a swap, meaning an attacker could execute code in a staging slot or alternate version and potentially evade detection, since the primary production deployment remains untouched.

For example, in Azure App Service, an attacker who compromises a staging deployment slot could either swap it into production, thus pushing malicious code live, or exploit the slot's separate URL to run the malicious app without modifying the production's code.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7021](../mitigations/Restrict%20environment%20management%20permissions.md)|Restrict environment management permissions|Limit RBAC permissions to prevent unauthorized creation, modification, or swapping of deployment slots.|
|[MS-M7022](../mitigations/Require%20approval%20for%20promotions.md)|Require approval for promotions|Enforce manual approval gates or CI/CD controls before promoting staging or test environments to production.|