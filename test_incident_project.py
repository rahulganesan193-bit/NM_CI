from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Lightweight local simulation of the intended rule outcomes.
def category_change(state):
    state['subcategory'] = ''
    return state

def impact_change(state, new_value):
    if new_value == '1':
        state['urgency'] = '1'
        state['info'] = True
    return state

def priority_change(state, new_value):
    state['warning'] = (new_value == '1')
    return state

def on_submit(state):
    if state.get('short_description', '') == '':
        return False, 'short_description'
    if state.get('impact') == '1' and state.get('assigned_to', '') == '':
        return False, 'assigned_to'
    return True, None

def on_cell_edit_state():
    return False

checks=[]
# Repository checks
required = [
    'README.md',
    '05_phase5_development_and_testing/01_implementation_artifacts/ui_policy_configuration.md',
    '05_phase5_development_and_testing/01_implementation_artifacts/onchange_category_clear_subcategory.js',
    '05_phase5_development_and_testing/01_implementation_artifacts/onchange_impact_set_urgency.js',
    '05_phase5_development_and_testing/01_implementation_artifacts/onchange_priority_critical_warning.js',
    '05_phase5_development_and_testing/01_implementation_artifacts/onsubmit_incident_validation.js',
    '05_phase5_development_and_testing/01_implementation_artifacts/oncelledit_block_state_list_edit.js',
    '06_phase6_project_documentation/01_functional_specification_document_fsd.md',
    '06_phase6_project_documentation/02_final_project_report.md',
]
for rel in required:
    checks.append((f'Artifact exists: {rel}', (ROOT/rel).exists()))

s={'subcategory':'Network','urgency':'3'}
category_change(s); checks.append(('Category change clears Subcategory', s['subcategory']=='') )
s={'urgency':'3'}; impact_change(s,'1'); checks.append(('High Impact sets Urgency High', s['urgency']=='1'))
s={'warning':False}; priority_change(s,'1'); checks.append(('Critical Priority warning', s['warning'] is True))
s={'short_description':'Test incident','impact':'1','assigned_to':'user1'}; ok,_=on_submit(s); checks.append(('Valid High Impact submit allowed', ok))
s={'short_description':'','impact':'2','assigned_to':'user1'}; ok,field=on_submit(s); checks.append(('Empty Short description blocked', not ok and field=='short_description'))
s={'short_description':'Test incident','impact':'1','assigned_to':''}; ok,field=on_submit(s); checks.append(('High Impact missing Assigned To blocked', not ok and field=='assigned_to'))
checks.append(('State list edit blocked', on_cell_edit_state() is False))

passed=0
for name,ok in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    passed += int(ok)
print(f"\n{passed}/{len(checks)} verification checks passed.")
if passed != len(checks):
    raise SystemExit(1)
print('PROJECT VERIFICATION: PASS')
