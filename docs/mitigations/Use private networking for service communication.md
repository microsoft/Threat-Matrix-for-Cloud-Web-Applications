---
hide:
  - toc
  - footer
---

# Use Private Networking for Service Communication

!!! info inline end
    ID: MS-M7035<br>
    MITRE mitigation: [M1030](https://attack.mitre.org/mitigations/M1030/)

Connect cloud services via private endpoints, VPC peering, or VNET integration to avoid exposing service URLs on public networks. Private networking reduces the attack surface and prevents discovery of internal service endpoints.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7021](../techniques/Cloud%20service%20discovery.md)|Cloud service discovery|Connect cloud services via private endpoints, VPC peering, or VNET integration to avoid exposing service URLs.|
