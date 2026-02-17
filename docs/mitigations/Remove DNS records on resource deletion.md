---
hide:
  - toc
  - footer
---

# Remove DNS Records on Resource Deletion

!!! info inline end
    ID: MS-M7001<br>
    MITRE mitigation: -

Ensure that DNS records pointing to cloud resources are promptly deleted or updated when the associated services are decommissioned. This prevents dangling DNS entries that could be exploited for subdomain takeover attacks.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7001](../techniques/Subdomain%20takeover.md)|Subdomain takeover|Delete or update DNS entries immediately when decommissioning cloud applications or services to prevent subdomain takeover.|
