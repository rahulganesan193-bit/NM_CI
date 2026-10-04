# Phase 3: Proposed Solution
## 1. Executive Summary
The proposed solution combines one core UI Policy with focused Client Scripts.
## 2. Proposed Functional Design
### 2.1. High Impact Control UI Policy
Condition: `Impact is 1 - High`.
### 2.2. Assignment Group Mandatory Action
Assignment group is mandatory while the condition is true.
### 2.3. Urgency Read-Only Action
Urgency is read-only while the condition is true.
### 2.4. Reverse if false
Policy actions reverse when Impact is no longer High.
## 3. Client Script Design
### 3.1. onLoad Script
Initializes the Incident form and can provide lightweight user guidance.
### 3.2. Category onChange Script
Clears `subcategory` whenever `category` changes.
### 3.3. Impact onChange Script
Sets `urgency` to High when Impact is High and displays an informational message.
### 3.4. Priority onChange Script
Warns the user when Priority is Critical.
### 3.5. onSubmit Script
Validates Short description and blocks High-impact save when Assigned To is empty.
### 3.6. onCellEdit Script
Blocks direct State list editing and instructs the user to open the Incident.
## 4. Exception Handling
Empty values are checked before updates. Validation returns false only when a defined rule is violated.
## 5. State and Event Transition Model
```text
Impact changes → UI Policy evaluation + Impact onChange
Category changes → Subcategory reset
Priority changes → Critical warning
Submit → validation → save / correction
List State edit → block
```
## 6. Design Acceptance Criteria
Every defined requirement has a corresponding artifact and UAT scenario.
