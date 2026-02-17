---
hide:
  - toc
  - footer
---

# Exposed/misconfigured admin interfaces

!!! info inline end
    ID: MS-TA7005<br>
    Tactic: [Initial Access](../tactics/InitialAccess/index.md)<br>
    MITRE technique: 

Some cloud-based web applications expose administrative interfaces for managing deployments, configurations, or runtime operations. If these interfaces are exposed to the internet or misconfigured, attackers might be able to access them and view critical data, execute commands, or manipulate application behavior.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7011](../mitigations/Disable%20basic%20authentication.md)|Disable basic authentication|If possible, turn off user/password authentication on administrative interfaces such as SCM endpoints, function management consoles, and deployment portals.|
|[MS-M7012](../mitigations/Enforce%20multi-factor%20authentication%20(MFA).md)|Enforce multi-factor authentication (MFA)|Require MFA for access to all administrative and management interfaces.|
|[MS-M7013](../mitigations/Restrict%20network%20access%20to%20sensitive%20services.md)|Restrict network access to sensitive services|Limit access to administrative endpoints using IP allowlists, private networking, or VPN requirements.|
|[MS-M7014](../mitigations/Implement%20role-based%20access%20control%20(RBAC).md)|Implement role-based access control (RBAC)|Ensure only authorized roles can access administrative features and interfaces.|
