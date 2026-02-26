---
hide:
  - toc
  - footer
---

# Instance metadata API

!!! info inline end
    ID: MS-TA7022<br>
    Tactic: [Discovery](../tactics/Discovery/index.md)<br>
    MITRE technique: [T1526](https://attack.mitre.org/techniques/T1526/)

Cloud platforms expose metadata services that provide information about the running environment, such as instance details, network configuration, and identity credentials. In some cases, this service is available from within cloud web applications as well. Attackers who gain access to such application may query the metadata API service for getting information about the underlying VM and the application environment.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7027](../mitigations/Restrict%20access%20to%20metadata%20services.md)|Restrict access to metadata services|Block or limit access to metadata endpoints from within applications unless required for specific functionality.|
|[MS-M7036](../mitigations/Disable%20legacy%20metadata%20endpoints.md)|Disable legacy metadata endpoints|Turn off IMDSv1 or unauthenticated metadata access where supported.|
