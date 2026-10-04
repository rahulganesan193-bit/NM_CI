# Incident Client Script & UI Policy Configuration Guide
## 🎯 Project Overview
Configure the Incident table with one UI Policy and six Client Scripts.
## 🛠️ Step-by-Step Instructions
### Step 1: Open UI Policies
System UI → UI Policies → New.
### Step 2: Configure High Impact Control
Table Incident; condition Impact is 1 - High; Active true; Reverse if false true.
### Step 3: Add Assignment Group Action
Field Assignment group; Mandatory true.
### Step 4: Add Urgency Action
Field Urgency; Read-only true.
### Step 5: Create Client Scripts
Create the six scripts from `05_phase5_development_and_testing/01_implementation_artifacts/` with their stated event types.
### Step 6: Test and Save
Use the UAT plan and test cases.
## 🔍 Execution Verification
Set Impact to High, verify mandatory/read-only behavior and automatic Urgency. Then test submit validation and State list edit blocking.
