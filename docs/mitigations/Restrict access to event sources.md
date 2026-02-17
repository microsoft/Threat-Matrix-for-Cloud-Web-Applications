---
hide:
  - toc
  - footer
---

# Restrict Access to Event Sources

!!! info inline end
    ID: MS-M7015<br>
    MITRE mitigation: -

Limit who can publish messages to queues, upload files to storage, or invoke triggers that activate serverless functions. Controlling access to event sources prevents unauthorized triggering of backend workflows.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7006](../techniques/Serverless%20trigger%20injection.md)|Serverless trigger injection|Limit who can publish messages to queues, upload files to storage, or invoke HTTP triggers that activate serverless functions.|
