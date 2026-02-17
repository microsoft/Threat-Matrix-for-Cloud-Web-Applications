---
hide:
  - toc
  - footer
---

# Restrict Network Access to Sensitive Services

!!! info inline end
    ID: MS-M7013<br>
    MITRE mitigation: [M1035](https://attack.mitre.org/mitigations/M1035/)

Limit access to sensitive interfaces such as admin consoles, databases, storage buckets, and service-to-service APIs by using IP allowlists, private networking, or VPN requirements. This reduces the attack surface by preventing access from unauthorized networks.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7005](../techniques/Exposed%20misconfigured%20admin%20interfaces.md)|Exposed/misconfigured admin interfaces|Limit access to administrative endpoints using IP allowlists, private networking, or VPN requirements.|
|[MS-TA7020](../techniques/Access%20to%20connected%20cloud%20storage.md)|Access to connected cloud storage|Use private endpoints, VPC/VNET integration, or firewall rules to limit storage access to authorized networks.|
|[MS-TA7025](../techniques/Access%20application%20database.md)|Access application database|Use private endpoints, VPC/VNET integration, or firewall rules to prevent direct internet access to databases.|
