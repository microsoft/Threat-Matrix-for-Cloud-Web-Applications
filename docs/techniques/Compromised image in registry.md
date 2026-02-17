---
hide:
  - toc
  - footer
---

# Compromised image in registry

!!! info inline end
    ID: MS-TA7004<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md)<br>
    MITRE technique: [T1195.002](https://attack.mitre.org/techniques/T1195/002/), [T1525](https://attack.mitre.org/techniques/T1525/)

Some cloud web applications are deployed from a container image pulled from private or public registries. Attackers who get access to a private registry can plant their own compromised images or update an existing image with malicious code, which will run the next time the web application pulls the container image.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7008](../mitigations/Secure%20CI%20CD%20pipelines.md)|Secure CI/CD pipelines|Placing gates in the CI/CD process can block pushing unsecured code to container images.|
|[MS-M7010](../mitigations/Image%20assurance%20policy.md)|Image assurance policy|Ensure that only images that passed the security compliance policies are pushed to registries and deployed.|
