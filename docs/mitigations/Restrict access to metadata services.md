---
hide:
  - toc
  - footer
---

# Restrict Access to Metadata Services

!!! info inline end
    ID: MS-M7027<br>
    MITRE mitigation: [M1035](https://attack.mitre.org/mitigations/M1035/)

Block or limit application access to instance metadata endpoints (IMDS) unless explicitly required for legitimate functionality. This prevents attackers from querying metadata services to obtain credentials or sensitive environment information.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7016](../techniques/Access%20workload%20identity%20credentials.md)|Access workload identity credentials|Block or limit application access to instance metadata endpoints (IMDS) unless explicitly required for legitimate functionality.|
|[MS-TA7022](../techniques/Instance%20metadata%20API.md)|Instance metadata API|Block or limit access to metadata endpoints from within applications unless required for specific functionality.|
