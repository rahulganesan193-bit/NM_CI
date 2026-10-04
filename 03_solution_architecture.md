# Phase 3: Solution Architecture
## 1. Architecture Overview
The solution uses the standard Incident form as the presentation layer and native client-side configuration as the control layer.
## 2. Four-Tier Solution Architecture
### Tier 1: User Interface
Incident form and list.
### Tier 2: Client Control Layer
UI Policies, UI Policy Actions and Client Scripts.
### Tier 3: ServiceNow Runtime
Client script engine and `g_form` APIs.
### Tier 4: Data Layer
Incident table and reference data.
## 3. Entity-Relationship Model
```text
sys_user ──< incident >── sys_user_group
                    |
                    +── category/subcategory choices
```
## 4. State Machine and Event Model
### 4.1. Form State
Open → Edit → Validate → Save / Correct.
### 4.2. High Impact Policy State
Impact High → Assignment group mandatory + Urgency read-only.
### 4.3. List Edit State
State edit attempted → onCellEdit → callback(false) → unchanged.
## 5. RBAC and Governance Model
UI controls improve usability but do not replace ACLs or server-side security.
## 6. Architecture Decision and Sign-Off
Native UI Policies and Client Scripts are selected for the project scope.
