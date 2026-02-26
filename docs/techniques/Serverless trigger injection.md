---
hide:
  - toc
  - footer
---

# Serverless trigger injection

!!! info inline end
    ID: MS-TA7006<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md)<br>
    MITRE technique: 

In cases where the application executes backend workflows in response to event-driven triggers, an end user who can directly or indirectly influence those triggers may cause unintended activity within the application. By manipulating inputs such as crafted file uploads, queue messages, API calls, or other event sources, an attacker can force serverless functions to run with their supplied data, which could lead to unintended code execution, data access, or further compromise.

For example, an attacker might upload a modified image file containing a crafted payload through a legitimate web form. The image is then stored in an S3 bucket, which triggers an AWS Lambda function configured to process new uploads. If the function handles the file without proper validation, the attacker's payload could cause unintended behavior or even lead to remote code execution.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7015](../mitigations/Restrict%20access%20to%20event%20sources.md)|Restrict access to event sources|Limit who can publish messages to queues, upload files to storage, or invoke HTTP triggers that activate serverless functions.|
|[MS-M7016](../mitigations/Enforce%20input%20validation%20and%20sanitization.md)|Enforce input validation and sanitization|Validate all event inputs (message payloads, file metadata, API parameters) against strict schemas before processing.|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Grant serverless functions only the permissions necessary to complete their tasks.|
|[MS-M7006](../mitigations/Deploy%20a%20web%20application%20firewall%20(WAF).md)|Deploy a web application firewall (WAF)|Use WAF or API Gateway validation to filter malicious inputs before they reach serverless functions.|
