---
hide:
  - toc
  - footer
---

# Denial of wallet

!!! info inline end
    ID: MS-TA7030<br>
    Tactic: [Impact](../tactics/Impact/index.md)<br>
    MITRE technique: 

Cloud applications often scale dynamically based on demand, incurring costs for compute, storage, and data transfer. Attackers may intentionally trigger operations that will cause those resources to scale out to impose financial damage. For example, attackers can flood a web application with requests, similarly to traditional denial-of-service (DoS) attacks. This will cause the application to allocate more resources, thus causing increased charges.
For example, an attacker could repeatedly invoke a Cloud Function with high memory allocation, leading to inflated billing due to excessive execution time.

## Mitigations

|ID|Mitigation|Description|
|--|----------|-----------|
|[MS-M7032](../mitigations/Implement%20rate%20limiting.md)|Implement rate limiting|Throttle API requests, function invocations, and user-triggered operations to prevent abuse.|
|[MS-M7043](../mitigations/Configure%20cost%20guardrails%20and%20spending%20alerts.md)|Configure cost guardrails and spending alerts|Set budget limits with automatic alerts and optional service shutdowns when thresholds are exceeded.|
|[MS-M7044](../mitigations/Implement%20resource%20quotas%20and%20concurrency%20limits.md)|Implement resource quotas and concurrency limits|Cap maximum function executions, API requests, and scaling behavior to prevent runaway costs.|