---
hide:
  - toc
  - footer
---

# Subdomain takeover

!!! info inline end
    ID: MS-TA7001<br>
    Tactic: [Resource Development](../tactics/ResourceDevelopment/index.md)<br>
    MITRE technique: [T1584.001](https://attack.mitre.org/techniques/T1584/001/)

Deleting a cloud application or service without removing its associated DNS record can leave the organization susceptible to subdomain takeover. An attacker who registers a resource at the same address (e.g., a cloud function, app service, or storage endpoint) can hijack traffic intended for the original service, potentially serving malicious content or harvesting credentials.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7001](../mitigations/Remove%20DNS%20records%20on%20resource%20deletion.md)|Remove DNS records on resource deletion|Delete or update DNS entries immediately when decommissioning cloud applications or services to prevent subdomain takeover.|
|[MS-M7002](../mitigations/Implement%20domain%20ownership%20verification.md)|Implement domain ownership verification|Use cloud provider domain verification mechanisms to ensure only authorized services can claim domains.|
|[MS-M7003](../mitigations/Use%20randomized%20service%20endpoints.md)|Use randomized service endpoints|Some cloud providers offer to add a random suffix to the site name, making it unique even after deletion.|
