# Data Flow Diagrams (DFD) & Agile User Stories
## 1. Executive Summary
This document defines the Incident data flow and the user stories implemented through UI Policies and Client Scripts.
## 2. Data Flow Architecture
### 2.1. DFD Level 0: Incident Context Diagram
```text
User --> Incident Form --> Client Controls --> Incident Record
                 ^              |
                 |--------------|
```
#### Inbound & Outbound Data Stream Catalog (Level 0)
| Stream | Direction | Description |
|---|---|---|
| Incident field values | User → Form | Data entered by user |
| Dynamic feedback | Form → User | Warning/error/read-only behavior |
| Valid record | Form → Incident | Successful save |
### 2.2. DFD Level 1: Functional Process Decomposition Diagram
```text
P1 Load Form -> P2 Field Change Handling -> P3 UI Policy Evaluation -> P4 Submit Validation -> P5 Save
```
#### Detailed Process Specifications (Level 1)
P1 initializes; P2 responds to Category/Impact/Priority; P3 applies conditional mandatory/read-only behavior; P4 validates; P5 persists valid data.
## 3. ServiceNow Core Data Dictionary & Schema Specifications
### 3.1. Incident Table (`incident`)
Primary table for the project.
### 3.2. Incident Fields
Important fields include `short_description`, `category`, `subcategory`, `impact`, `urgency`, `priority`, `assignment_group`, `assigned_to`, and `state`.
### 3.3. Client Script Configuration (`sys_script_client`)
Stores client-side scripts and their event types.
### 3.4. UI Policy Configuration (`sys_ui_policy`)
Stores conditional form policies.
### 3.5. UI Policy Action Configuration (`sys_ui_policy_action`)
Stores field-level actions such as mandatory and read-only.
### 3.6. User and Group References (`sys_user`, `sys_user_group`)
Provide Assignment group and Assigned To reference data.
## 4. Agile Epics & User Stories
### Epic Structure Overview
### 4.1. Epic 1: Incident Form Quality
#### User Story US-01: Validate Short Description
As a service desk user, I want an error when Short description is invalid so that every submitted Incident has usable summary information.
#### User Story US-02: Clear Dependent Subcategory
As a user, I want Subcategory cleared when Category changes so that invalid combinations are not submitted.
### 4.2. Epic 2: Dynamic Severity and Routing Controls
#### User Story US-03: Enforce High Impact Assignment Group
As a service desk user, I want Assignment group mandatory for High Impact.
#### User Story US-04: Control High Impact Urgency
As a user, I want Urgency automatically set to High and read-only for High Impact.
#### User Story US-05: Warn on Critical Priority
As a user, I want an immediate warning when Priority is Critical.
### 4.3. Epic 3: Save and List Protection
#### User Story US-06: Validate Assigned To
As a service desk user, I want High-impact records blocked when Assigned To is empty.
#### User Story US-07: Protect State from List Editing
As an administrator, I want direct State list edits blocked.
#### User Story US-08: Allow Form-Based State Updates
As a user, I want valid State changes through the Incident form.
## 5. Requirements Traceability Matrix (User Stories vs System Components)
| Story | UI Policy | onChange | onSubmit | onCellEdit |
|---|---|---|---|---|
| US-01 | | | ✓ | |
| US-02 | | ✓ | | |
| US-03 | ✓ | | | |
| US-04 | ✓ | ✓ | | |
| US-05 | | ✓ | | |
| US-06 | | | ✓ | |
| US-07 | | | | ✓ |
| US-08 | | | | ✓ |
