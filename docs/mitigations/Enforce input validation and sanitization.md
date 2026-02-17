---
hide:
  - toc
  - footer
---

# Enforce Input Validation and Sanitization

!!! info inline end
    ID: MS-M7016<br>
    MITRE mitigation: [M1013](https://attack.mitre.org/mitigations/M1013/)

Validate and sanitize all inputs before processing, including event payloads, file metadata, API parameters, and user-supplied data. Use strict schemas and allowlists to ensure inputs conform to expected formats.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7006](../techniques/Serverless%20trigger%20injection.md)|Serverless trigger injection|Validate all event inputs (message payloads, file metadata, API parameters) against strict schemas before processing.|
|[MS-TA7024](../techniques/Server%20side%20request%20forgery%20(SSRF).md)|Server side request forgery (SSRF)|Normalize URLs, strip credentials, and validate against known-safe patterns before making requests.|
