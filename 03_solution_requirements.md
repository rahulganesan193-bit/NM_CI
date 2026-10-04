# Solution Requirements Specification: Functional, Non-Functional & Service Level Agreements
## 1. Executive Summary
The requirements define deterministic client-side controls for Incident records.
## 2. Functional Requirements (FR)
| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Validate Short description on submit | High |
| FR-02 | Clear Subcategory on Category change | High |
| FR-03 | Warn when Priority = 1 - Critical | Medium |
| FR-04 | Assignment group mandatory for Impact = 1 - High | High |
| FR-05 | Urgency read-only for Impact = 1 - High | High |
| FR-06 | Set Urgency = 1 - High for Impact = 1 - High | High |
| FR-07 | Block save when High Impact and Assigned To is empty | High |
| FR-08 | Block State list editing | High |
## 3. Non-Functional Requirements (NFR)
### 3.1. NFR-01: Performance & Execution Latency
Scripts should execute quickly during normal form interaction.
### 3.2. NFR-02: Security, Governance & Role-Based Access Control (RBAC)
Client-side controls supplement, but do not replace, server-side security and ACLs.
### 3.3. NFR-03: High Availability, Fault Tolerance & Idempotency
Scripts should avoid unnecessary repeated updates and handle empty values safely.
### 3.4. NFR-04: Usability & Multi-Device Accessibility
Messages should be concise and field-specific.
### 3.5. NFR-05: Auditability & Compliance Logging
Configuration should be documented and traceable to requirements.
### 3.6. NFR-06: Maintainability, Upgradeability & LTS Longevity
Use standard `g_form` APIs and focused scripts.
## 4. Platform Technical Constraints & Design Assumptions
### 4.1. Technical Constraints
The solution depends on standard ServiceNow Incident fields and client scripting support.
### 4.2. Design Assumptions
The field values use standard Incident choice values: Impact High = `1`, Urgency High = `1`, Priority Critical = `1`.
## 5. Service Level Agreement (SLA) & Operational Level Agreement (OLA) Hierarchy
### 5.1. SLA / OLA Matrix & Governance Rules
This micro-project focuses on data-entry behavior rather than production SLA measurement. The rules are intended to reduce preventable data-quality issues before submission.
## 6. Requirements Traceability Matrix (FRTM)
| Requirement | Artifact |
|---|---|
| FR-01 | onsubmit_incident_validation.js |
| FR-02 | onchange_category_clear_subcategory.js |
| FR-03 | onchange_priority_critical_warning.js |
| FR-04 | UI Policy High Impact Control |
| FR-05 | UI Policy Action Urgency |
| FR-06 | onchange_impact_set_urgency.js |
| FR-07 | onsubmit_incident_validation.js |
| FR-08 | oncelledit_block_state_list_edit.js |
