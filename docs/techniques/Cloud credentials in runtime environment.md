---
hide:
  - toc
  - footer
---

# Cloud credentials in runtime environment

!!! info inline end
    ID: MS-TA7019<br>
    Tactic: [Credential Access](../tactics/CredentialAccess/index.md)<br>
    MITRE technique: [T1552](https://attack.mitre.org/techniques/T1552/)

Some web applications store secrets such as keys, tokens, and connection strings in environment variables or configuration files. In cloud environments, those secrets are often used to access additional cloud services within the environment. If an attacker gains access, even read-only, to the running application environment, they would be able to retrieve those credentials and use them to authenticate against those external cloud resources.

For example, if an attacker gains access to the environment variables of an Azure Function with an integrated Azure OpenAI resource, they could extract the endpoint and key of the AI resource from those variables, which grants them full access to the Azure OpenAI service's API for this resource.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7026](../mitigations/Use%20workload%20identities%20instead%20of%20static%20credentials.md)|Use workload identities instead of static credentials|Avoid storing cloud credentials directly in environment variables or configuration files.|
|[MS-M7020](../mitigations/Use%20secrets%20management%20solutions.md)|Use secrets management solutions|Store secrets in dedicated secret managers and retrieve them dynamically at runtime using identity-based access.|
|[MS-M7033](../mitigations/Restrict%20access%20to%20configuration%20endpoints.md)|Restrict access to configuration endpoints|Disable or secure application configuration endpoints that expose environment variables or settings.|