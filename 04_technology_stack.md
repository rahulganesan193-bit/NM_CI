# Technology Stack & Platform Architecture Specification
## 1. Executive Summary
The solution is implemented using native ServiceNow Incident configuration with UI Policies, UI Policy Actions and Client Scripts.
## 2. Multi-Tiered System Architecture
```text
Presentation: Incident Form/List
        ↓
Client Control: UI Policies + Client Scripts
        ↓
ServiceNow Runtime: g_form / Client Script engine
        ↓
Data: incident table and reference fields
```
## 3. Platform Runtime & Version Compatibility
### Platform Runtime Configuration
Use a supported ServiceNow release with standard Incident fields and client-side APIs.
## 4. Client Script Module Architecture
### 4.1. Event Mechanics & Client Runtime
onLoad initializes, onChange reacts to field changes, onSubmit validates save, and onCellEdit controls list editing.
### 4.2. g_form API Binding Specifications
The implementation uses `getValue`, `setValue`, `showFieldMsg`, `showErrorBox`, `setMandatory`, and related standard APIs as required.
## 5. Incident Form & Client-Side Component Architecture
### 5.1. Incident Table Configuration (`incident`)
The Incident table is the target table.
### 5.2. UI Policy Architecture (`sys_ui_policy`)
The High Impact Control policy evaluates Impact.
### 5.3. Client-Side Policies & Scripts
Six focused script artifacts are provided.
## 6. Core Relational Schema & Table Descriptions
### Table Relationships & Referential Integrity
Incident references users and groups through Assigned To and Assignment group.
## 7. Enterprise Integration Points
### 7.1. Identity & Directory Synchronization
User and group reference data is supplied by ServiceNow identity configuration.
### 7.2. Notification Gateway
The project uses client-side messages; production notifications remain a separate ServiceNow configuration concern.
### 7.3. External Integration Hooks
No external integration is required for the core project.
## 8. Security Architecture, Role-Based Access (RBAC) & Governance
### Data Security & Governance Compliance
Client scripts are not treated as a security boundary. ACLs and server-side controls remain authoritative.
## 9. Upgrade Readiness & Automated Testing (ATF)
The repository includes a local verification suite and UAT matrix. ServiceNow ATF can be used for live instance testing.
