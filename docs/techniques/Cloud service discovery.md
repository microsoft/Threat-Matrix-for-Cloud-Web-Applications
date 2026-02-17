---
hide:
  - toc
  - footer
---

# Cloud service discovery

!!! info inline end
    ID: MS-TA7021<br>
    Tactic: [Discovery](../tactics/Discovery/index.md)<br>
    MITRE technique: [T1526](https://attack.mitre.org/techniques/T1526/)

Cloud‑hosted applications often contain configuration values or runtime information that reference other cloud services the application interacts with, such as Service URL, API endpoints. After gaining access to a web application, attackers can discover additional cloud resources through environment variables, network connections or application code.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7035](../mitigations/Use%20private%20networking%20for%20service%20communication.md)|Use private networking for service communication|Connect cloud services via private endpoints, VPC peering, or VNET integration to avoid exposing service URLs.|
