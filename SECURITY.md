# Security Policy

The **JLDesignNetwork** and the **Vampire TTRPG Framework** project take security seriously. We appreciate the responsible disclosure of any potential vulnerabilities or exploits found within our build pipelines, automation scripts, or repository infrastructure.

---

## 1. Supported Versions

Security updates and forensic validations are actively applied to the current and recent Generational Versioning Schema (GVS) release milestones:

| Version / Epoch | Supported | Status |
| :--- | :---: | :--- |
| **`2608.x`** (Current Generation) | ✅ | **Active Support & Security Maintenance** |
| **`< 2608.0`** (Legacy Versions) | ❌ | Deprecated / Unsupported |

---

## 2. Reporting a Vulnerability

### A. Preferred Method: Private Vulnerability Reporting
We have enabled **Private Vulnerability Reporting** on this repository. To privately disclose a vulnerability:
1. Navigate to the **[Security tab](https://github.com/JLDesignNetwork/Vampire-TTRPG-Framework/security)** of this repository.
2. Under the left-hand navigation, click **Advisories**.
3. Click **"Report a vulnerability"** to open a private disclosure draft directly with the repository maintainers.

### B. What to Include in Your Report
To help us triage and resolve the issue quickly, please provide:
* **Description:** A clear overview of the potential vulnerability or exploit.
* **Affected Component:** The specific file, script (`build_ruleset.py`, `validate_workspace.py`, etc.), or workflow.
* **Reproduction Steps:** Step-by-step instructions or proof-of-concept demonstrating the issue.
* **Impact Assessment:** The potential impact (e.g., unauthorized code execution, CI pipeline poisoning, credential leakage).

---

## 3. Our Security Response Protocol

* **Acknowledgment:** We strive to acknowledge received reports within **48 hours**.
* **Triage & Remediation:** Valid vulnerabilities are audited via our **🔴 Red Team Adversarial Protocol** and patched with high priority.
* **Public Disclosure:** Security fixes will be released alongside an updated GVS subversion and credited in `CHANGELOG.md` (unless the reporter requests anonymity).

Thank you for helping keep the **Vampire TTRPG Framework** secure!
