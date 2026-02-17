---
hide:
  - toc
  - footer
---

# Disable Basic Authentication

!!! info inline end
    ID: MS-M7011<br>
    MITRE mitigation: [M1042](https://attack.mitre.org/mitigations/M1042/)

Disable username/password authentication on administrative interfaces, deployment endpoints, and legacy protocols where possible. Basic authentication is vulnerable to brute-force attacks and credential theft, and should be replaced with more secure authentication methods.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7005](../techniques/Exposed%20misconfigured%20admin%20interfaces.md)|Exposed/misconfigured admin interfaces|If possible, turn off user/password authentication on administrative interfaces such as SCM endpoints, function management consoles, and deployment portals.|
|[MS-TA7010](../techniques/Cloud%20native%20terminal.md)|Cloud native terminal|Turn off username/password authentication where possible.|
|[MS-TA7018](../techniques/Brute%20force.md)|Brute force|Remove username/password authentication from deployment endpoints, admin interfaces, and legacy protocols.|
|[MS-TA7026](../techniques/Event%20data%20capture.md)|Event data capture|Turn off basic authentication for log streaming endpoints and diagnostic interfaces.|
