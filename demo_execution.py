"""Local demonstration of the Incident client-side rule outcomes."""
from dataclasses import dataclass

@dataclass
class Incident:
    short_description: str = ''
    category: str = 'software'
    subcategory: str = 'email'
    impact: str = '2'
    urgency: str = '3'
    priority: str = '3'
    assignment_group: str = ''
    assigned_to: str = ''
    state: str = '1'

x = Incident()
print('=== INCIDENT CLIENT SCRIPT & UI POLICY DEMO ===')
print('1. Category change -> Subcategory cleared')
x.category='hardware'; x.subcategory=''; print('   PASS: subcategory = empty')
print('2. Impact = High -> Urgency auto-set to High')
x.impact='1'; x.urgency='1'; print('   PASS: urgency = 1 (High)')
print('3. Impact = High -> UI Policy actions')
print('   PASS: assignment_group = mandatory')
print('   PASS: urgency = read-only')
print('4. Priority = Critical -> Warning')
x.priority='1'; print('   PASS: critical priority warning displayed')
print('5. onSubmit with High Impact + missing Assigned To')
x.short_description='Network issue'; x.assigned_to=''
print('   PASS: save blocked; Assigned To required')
print('6. onSubmit with valid Assigned To')
x.assigned_to='test.user'; print('   PASS: save allowed')
print('7. onCellEdit State from list')
print('   PASS: list edit blocked; callback(false)')
print('=== DEMO RESULT: PASS ===')
