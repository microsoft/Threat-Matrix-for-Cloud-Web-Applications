---
hide:
  - toc
  - footer
---

# Access workload identity credentials

!!! info inline end
    ID: MS-TA7016<br>
    Tactic: [Privilege Escalation](../tactics/PrivilegeEscalation/index.md), [Credential Access](../tactics/CredentialAccess/index.md)<br>
    MITRE technique: [T1552.005](https://attack.mitre.org/techniques/T1552/005/)

Workload identities are identities that are managed by the cloud provider and can be allocated to cloud resources. The identity's secret is fully managed by the cloud provider, which eliminates the need to manage the credentials. Web apps can use workload identities to perform actions on other cloud resources by querying IMDS (or similar endpoints). Attackers who gain access to a web app can leverage their access to the IMDS endpoint to get the workload identity's token. With a token, the attackers can access cloud resources.

For example, in Azure App Services, the managed identity access token can be acquired through a local identity endpoint, which is defined in the environment variables (IDENTITY_ENDPOINT). If an attacker is able to execute code on such App Service instance, they would be able to query the endpoint and receive an access token to other Azure resources with the managed identity permissions.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7027](../mitigations/Restrict%20access%20to%20metadata%20services.md)|Restrict access to metadata services|Block or limit application access to instance metadata endpoints (IMDS) unless explicitly required for legitimate functionality.|
|[MS-M7017](../mitigations/Implement%20least-privilege%20access.md)|Implement least-privilege access|Grant workload identities (managed identities, IAM roles, or service accounts) only the minimum permissions needed for their function.|
|[MS-M7028](../mitigations/Require%20session-based%20metadata%20access.md)|Require session-based metadata access|Use IMDSv2 (AWS) or equivalent protections that require token-based sessions to access metadata APIs.|