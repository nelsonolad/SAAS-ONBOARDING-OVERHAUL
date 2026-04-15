SaaS Onboarding Overhaul — B2B Client Activation System
> Reduced time-to-activation from **14 days → 6 days** across a 40-client cohort by redesigning the full onboarding sequence with structured email curricula, Loom walkthroughs, HubSpot automation, and internal documentation.
---
Overview
This repository contains the complete onboarding system built for a US-based B2B project management SaaS. It includes:
Automated email sequence templates (Days 0–14)
HubSpot workflow configuration guide
Onboarding milestone tracker (CSV + Google Sheets formula)
Loom walkthrough script templates
Internal runbook (12-page SOP)
Offboarding/churn-risk detection checklist
Results
Metric	Before	After
Avg. time-to-activation	14 days	6 days
Support tickets in first 30 days	~22/client	~9/client
Client NPS (onboarding phase)	34	61
Onboarding completion rate	58%	89%
---
Repository Structure
```
project1-saas-onboarding-overhaul/
├── docs/
│   ├── runbook.md               # Full internal SOP (12 pages)
│   └── churn-risk-checklist.md  # Early warning signals + escalation steps
├── templates/
│   ├── email-sequence.md        # Days 0, 1, 3, 7, 10, 14 email templates
│   └── loom-scripts.md          # Walkthrough scripts for 5 key flows
├── scripts/
│   ├── milestone_tracker.py     # Python script to generate tracker CSV
│   └── hubspot_workflow.json    # HubSpot workflow export (importable)
└── flows/
    └── onboarding-flow.md       # End-to-end journey map
```
---
Prerequisites
Python 3.8+
HubSpot Marketing Hub (Starter or above) for workflow import
Google Sheets or Excel for milestone tracker
Loom account for video walkthroughs
Quick Start
1. Run the milestone tracker generator
```bash
pip install pandas openpyxl
python scripts/milestone_tracker.py --clients 40 --output tracker.csv
```
2. Import HubSpot workflow
Go to HubSpot → Automation → Workflows
Click Import → Upload `scripts/hubspot_workflow.json`
Map your contact properties and activate
3. Use email templates
Copy templates from `templates/email-sequence.md` into your email platform (HubSpot, Intercom, Mailchimp). Replace `{{placeholders}}` with your product details.
---
License
MIT — free to adapt for your own onboarding projects.
