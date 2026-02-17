---
hide:
  - toc
  - footer
---

# Restrict Outbound Network Access

!!! info inline end
    ID: MS-M7037<br>
    MITRE mitigation: [M1037](https://attack.mitre.org/mitigations/M1037/)

Use egress filtering and firewall rules to control and limit outbound traffic from applications and functions. Restricting outbound access prevents data exfiltration and unauthorized use of compute resources.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7024](../techniques/Server%20side%20request%20forgery%20(SSRF).md)|Server side request forgery (SSRF)|Restrict outbound requests to a predefined list of trusted domains or IP ranges.|
|[MS-TA7028](../techniques/Data%20theft.md)|Data theft|Use egress filtering and firewall rules to prevent unauthorized data exfiltration.|
|[MS-TA7031](../techniques/Resource%20hijacking.md)|Resource hijacking|Limit outbound traffic from applications and functions to explicitly approved domains or IP ranges to prevent misuse.|
