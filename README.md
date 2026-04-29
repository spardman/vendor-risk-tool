# 🛡️ Third-Party Risk Management (TPRM) Tool

This repository showcases a full-cycle GRC (Governance, Risk, and Compliance) automation project. It includes a functional vendor scoring tool, a formal security policy, and an automated audit trail.

## 📂 Project Navigation
*   **[Security Policy](./POLICY.md):** Defines the "Governance" and scoring weights used for assessments.
*   **[Scoring Tool](./score_vendor.py):** The Python-based "Risk Management" tool used to evaluate vendors.
*   **[Risk Register](./risk_register.csv):** The "Compliance" evidence and historical audit log.

---

## 🚀 How it Works
The tool automates vendor onboarding by evaluating three critical security controls:
1.  **MFA Implementation** (Weighted 40%)
2.  **Data Encryption** (Weighted 40%)
3.  **SOC 2 Compliance** (Weighted 20%)

### 🛠️ Execution Example
Testing was performed in a sandboxed **Virtual Machine environment** to ensure data integrity and secure execution.

![Assessment Demo](./assessment_demo.jpg)

---

## 📈 Key GRC Skills Demonstrated
*   **Governance:** Developing formal security policies and approval thresholds.
*   **Risk Management:** Quantifying risk using weighted scoring models.
*   **Compliance Automation:** Generating immutable audit logs (CSV) with automated timestamps.
*   **Technical Literacy:** Python scripting and version control (GitHub).
