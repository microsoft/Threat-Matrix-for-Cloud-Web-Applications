---
hide:
  - toc
  - footer
---

# Avoid Logging Sensitive Data

!!! info inline end
    ID: MS-M7039<br>
    MITRE mitigation: -

Configure logging filters to exclude passwords, API keys, tokens, personally identifiable information (PII), and other sensitive data from application logs. This prevents credential exposure through log access.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7026](../techniques/Event%20data%20capture.md)|Event data capture|Configure logging filters to exclude passwords, API keys, tokens, and PII from application logs.|
