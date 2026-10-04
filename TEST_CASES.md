# Quality Assurance Test Cases Matrix
## 🧪 Test Execution Matrix
| ID | Scenario | Expected Outcome |
|---|---|---|
| TC01 | Empty Short description on submit | Save blocked |
| TC02 | Category changes | Subcategory cleared |
| TC03 | Priority = Critical | Warning displayed |
| TC04 | Impact = High | Assignment group mandatory; Urgency read-only |
| TC05 | Impact = High | Urgency auto-set to High |
| TC06 | High Impact + empty Assigned To | Save blocked |
| TC07 | Impact High → Medium | Policy reverses |
| TC08 | State edited from list | Edit blocked |
| TC09 | State edited from form | Update allowed |
## 📋 Acceptance Criteria Checklist
- [ ] All scripts active in ServiceNow.
- [ ] UI Policy active.
- [ ] Reverse if false verified.
- [ ] Positive and negative UAT completed.
- [ ] Final report and deliverables packaged.
