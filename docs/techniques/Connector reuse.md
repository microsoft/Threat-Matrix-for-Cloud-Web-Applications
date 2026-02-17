---
hide:
  - toc
  - footer
---

# Connector reuse

!!! info inline end
    ID: MS-TA7023<br>
    Tactic: [Lateral Movement](../tactics/LateralMovement/index.md)<br>
    MITRE technique: 

Cloud applications may use managed connectors or integrations resources to interact with third-party services. These connectors might store authentication or authorization details that are separate from the web application identity (such as OAuth or Access Keys). A compromised user with permissions over the connector resource might be able to utilize those credentials and spread them into those platforms.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Restrict who can view or modify connector configurations containing third-party credentials.|
