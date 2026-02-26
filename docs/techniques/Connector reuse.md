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

Cloud applications may use managed connectors or integration resources to interact with third-party services such as email providers, SaaS platforms, databases, or messaging systems. These connectors sometimes store authentication or authorization details - such as OAuth tokens and access keys, that are separate from the web application's own identity, and thus could be reused across multiple applications. An attacker who compromises a user or identity with permissions over the connector resource can invoke those stored credentials to access the connected third-party services, enabling lateral movement beyond the cloud environment.

For example, in Azure Logic Apps, API connections are standalone resources that store authenticated sessions to external services, such as Office 365, Slack, or SQL databases. An attacker with sufficient permissions on the resource group can create a new app that uses existing API connectors — triggering actions on the connected services using the stored credentials without needing to extract the underlying secrets.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Restrict who can view or modify connector configurations containing third-party credentials.|