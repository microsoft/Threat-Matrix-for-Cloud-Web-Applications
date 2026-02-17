---
hide:
  - toc
  - footer
---

# Implement Resource Quotas and Concurrency Limits

!!! info inline end
    ID: MS-M7044<br>
    MITRE mitigation: -

Set maximum CPU, memory, execution time, and concurrency limits on serverless functions and applications. Resource quotas and concurrency limits prevent runaway resource consumption from attacks or misconfigurations, and protect against financial damage from excessive resource usage.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7031](../techniques/Resource%20hijacking.md)|Resource hijacking|Set maximum CPU, memory, execution time, and concurrency limits on serverless functions and applications.|
|[MS-TA7030](../techniques/Denial%20of%20wallet.md)|Denial of wallet|Cap maximum function executions, API requests, and scaling behavior to prevent runaway costs.|
