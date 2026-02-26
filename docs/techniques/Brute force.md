---
hide:
  - toc
  - footer
---

# Brute force

!!! info inline end
    ID: MS-TA7018<br>
    Tactic: [Credential Access](../tactics/CredentialAccess/index.md)<br>
    MITRE technique: [T1110](https://attack.mitre.org/techniques/T1110/)

Some web applications or interfaces may still use basic authentication, either for user access, administrative functions, or deployment interfaces. An attacker could try to gain access by repeatedly attempting credentials combinations, and upon finding valid credentials, use them to access and use the relevant privileges.

For example, Azure App Service exposes the Kudu management console (the SCM site) and FTP endpoints that support basic authentication. This includes user‑scoped deployment credentials, which are manually set by the user and shared across all App Services within a subscription that the user has access to. If an attacker is able to successfully guess those credentials, they could gain deployment access to multiple applications in the subscription.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7011](../mitigations/Disable%20basic%20authentication.md)|Disable basic authentication|Remove username/password authentication from deployment endpoints, admin interfaces, and legacy protocols.|
|[MS-M7031](../mitigations/Enforce%20strong%20password%20policies.md)|Enforce strong password policies|Require complex passwords that are resistant to brute-force attacks.|
|[MS-M7012](../mitigations/Enforce%20multi-factor%20authentication%20(MFA).md)|Enforce multi-factor authentication (MFA)|Require MFA to prevent credential-based access even if passwords are guessed.|
|[MS-M7032](../mitigations/Implement%20rate%20limiting.md)|Implement rate limiting|Throttle authentication attempts and temporarily lock accounts after repeated failures.|