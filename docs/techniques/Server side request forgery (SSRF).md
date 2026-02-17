---
hide:
  - toc
  - footer
---

# Server side request forgery (SSRF)

!!! info inline end
    ID: MS-TA7024<br>
    Tactic: [Lateral Movement](../tactics/LateralMovement/index.md)<br>
    MITRE technique: [T1210](https://attack.mitre.org/techniques/T1210/)

In some applications, user-controlled input is used in outbound requests made by the web service to fetch external content or validate data. If this input is not properly validated, attacker may be able to control the destination of the request and cause the application to send request to unintended endpoints. This includes resources that are available only through private networks if the web application can access it.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7037](../mitigations/Restrict%20outbound%20network%20access.md)|Restrict outbound network access|Restrict outbound requests to a predefined list of trusted domains or IP ranges.|
|[MS-M7016](../mitigations/Enforce%20input%20validation%20and%20sanitization.md)|Enforce input validation and sanitization|Normalize URLs, strip credentials, and validate against known-safe patterns before making requests.|
