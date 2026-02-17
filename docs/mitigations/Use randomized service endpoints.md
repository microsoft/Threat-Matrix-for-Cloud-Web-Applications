---
hide:
  - toc
  - footer
---

# Use Randomized Service Endpoints

!!! info inline end
    ID: MS-M7003<br>
    MITRE mitigation: -

Configure cloud services to use randomized suffixes in their endpoint names, making them unique and preventing reuse of the same endpoint address after resource deletion.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7001](../techniques/Subdomain%20takeover.md)|Subdomain takeover|Some cloud providers offer to add a random suffix to the site name, making it unique even after deletion.|
