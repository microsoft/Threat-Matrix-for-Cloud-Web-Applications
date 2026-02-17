---
hide:
  - toc
  - footer
---

# Disable Legacy Metadata Endpoints

!!! info inline end
    ID: MS-M7036<br>
    MITRE mitigation: [M1042](https://attack.mitre.org/mitigations/M1042/)

Turn off IMDSv1 or other unauthenticated metadata access endpoints where supported. Legacy metadata endpoints lack security controls and can be easily exploited by attackers to obtain sensitive information.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7022](../techniques/Instance%20metadata%20API.md)|Instance metadata API|Turn off IMDSv1 or unauthenticated metadata access where supported.|
