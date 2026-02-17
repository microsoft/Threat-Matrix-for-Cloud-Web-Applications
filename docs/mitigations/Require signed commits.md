---
hide:
  - toc
  - footer
---

# Require Signed Commits

!!! info inline end
    ID: MS-M7025<br>
    MITRE mitigation: [M1045](https://attack.mitre.org/mitigations/M1045/)

Enforce commit signing to verify the authenticity and integrity of code changes. Signed commits provide cryptographic proof of the author's identity and ensure code has not been tampered with.

## Techniques Addressed by Mitigation

|ID|Name|Use|
|--|----------|-----------|
|[MS-TA7014](../techniques/Source%20code%20modification.md)|Source code modification|Enforce commit signing to verify the authenticity of code changes.|
