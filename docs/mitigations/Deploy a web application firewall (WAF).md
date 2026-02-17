---
hide:
  - toc
  - footer
---

# Deploy a Web Application Firewall (WAF)

!!! info inline end
    ID: MS-M7006<br>
    MITRE mitigation: [M1037](https://attack.mitre.org/mitigations/M1037/)

Deploy a Web Application Firewall to inspect and filter HTTP traffic to web applications. WAF rules can block common attack vectors including SQL injection, cross-site scripting (XSS), command injection, and other OWASP Top 10 vulnerabilities.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7002](../techniques/Application%20vulnerability.md)|Application vulnerability|Use WAF rules to block common attack vectors like SQL injection, XSS, and command injection.|
|[MS-TA7006](../techniques/Serverless%20trigger%20injection.md)|Serverless trigger injection|Use WAF or API Gateway validation to filter malicious inputs before they reach serverless functions.|
|[MS-TA7009](../techniques/Application%20exploit%20(RCE).md)|Application exploit (RCE)|Block exploit attempts targeting deserialization, template injection, or command execution vulnerabilities.|
