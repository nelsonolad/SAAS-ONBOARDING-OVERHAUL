# Onboarding Runbook — Internal SOP

**Version:** 2.1  
**Owner:** Customer Success Team  
**Last Updated:** 2024-01-10  
**Applies To:** All new B2B customers on Professional and Enterprise plans

---

## Table of Contents

1. [Overview & Goals](#1-overview--goals)
2. [Pre-Onboarding Checklist](#2-pre-onboarding-checklist)
3. [Day 0 — Account Provisioning](#3-day-0--account-provisioning)
4. [Days 1–3 — Core Setup Phase](#4-days-13--core-setup-phase)
5. [Days 4–7 — Team Activation Phase](#5-days-47--team-activation-phase)
6. [Days 8–14 — Advanced & Activation Phase](#6-days-814--advanced--activation-phase)
7. [Churn Risk Protocol](#7-churn-risk-protocol)
8. [Handoff to Support Team](#8-handoff-to-support-team)
9. [Escalation Matrix](#9-escalation-matrix)
10. [Metrics & Reporting](#10-metrics--reporting)
11. [Templates & Resources](#11-templates--resources)

---

## 1. Overview & Goals

### Purpose
This runbook defines the standard process for onboarding new B2B customers from account creation through full activation. Its goal is to achieve **activation within 6 days** while maintaining a positive NPS and minimising early churn.

### Definition of "Activated"
A customer is considered activated when they have:
- Completed their profile
- Configured the core feature
- Invited at least one team member
- Completed at least one meaningful key action
- Not submitted a cancellation request

### Key Metrics to Track
| Metric | Target |
|--------|--------|
| Time to Activation | ≤ 6 days |
| 30-Day Ticket Volume | ≤ 10 per client |
| Onboarding NPS | ≥ 55 |
| Completion Rate | ≥ 85% |

---

## 2. Pre-Onboarding Checklist

Complete before Day 0 email is sent:

- [ ] CRM record created with correct contact info
- [ ] Plan tier confirmed (Starter / Pro / Enterprise)
- [ ] CSM assigned in HubSpot
- [ ] Welcome email personalised (company name, CSM name, support email)
- [ ] Calendly link active and CSM availability set for next 14 days
- [ ] Loom videos uploaded and links tested
- [ ] HubSpot workflow enrollment confirmed
- [ ] Slack channel created (Enterprise clients only): `#onboarding-{{company}}`

---

## 3. Day 0 — Account Provisioning

**Responsible:** CSM

**Actions:**
1. Confirm account is live in the production environment
2. Verify login credentials were sent to the primary contact
3. Trigger HubSpot workflow enrollment manually if auto-trigger fails
4. Send a personal Slack/LinkedIn message to the primary contact (Enterprise only)
5. Log first entry in the milestone tracker

**Common Issues:**
- *Login email not received:* Check spam folder first; if not found, re-trigger from admin panel under Users → Resend Welcome
- *Wrong email address:* Update in CRM and re-trigger; do not send to incorrect address

---

## 4. Days 1–3 — Core Setup Phase

**Goal:** Client has core feature configured and understands the product basics.

**CSM Actions:**
- Monitor HubSpot email open rates daily
- If Day 1 email unopened by EOD Day 2 → send manual follow-up from personal email
- Check Loom video view stats; if unwatched → send direct link with personal note

**Milestone Checks (Day 3 EOD):**
- [ ] Day 0 email opened
- [ ] Login confirmed (check last active date in admin)
- [ ] Core feature status: configured / not configured

**If core feature not configured by Day 3:**
→ Send Loom video with direct link to setup page  
→ Offer 15-min setup call via Calendly  
→ Log as "Setup Assistance Needed" in tracker

---

## 5. Days 4–7 — Team Activation Phase

**Goal:** At least one team member invited; client using product with their team.

**CSM Actions:**
- Review Day 7 check-in email responses (monitored reply-to inbox)
- Conduct manual milestone review in tracker
- Book Day 7 check-in call for at-risk clients

**Milestone Checks (Day 7 EOD):**
- [ ] Team member(s) invited
- [ ] At least 1 collaborative action completed
- [ ] Client responded to Day 7 check-in email (or call completed)

**Churn Signal Flags:**
- Zero logins since Day 1
- No team members invited
- Two or more emails unopened
- Support ticket submitted about cancellation

→ See Section 7: Churn Risk Protocol

---

## 6. Days 8–14 — Advanced & Activation Phase

**Goal:** Client reaches full activation; NPS collected; handoff to support team initiated.

**CSM Actions:**
- Send Advanced Feature email (Day 10) — review personalisation before sending
- Review Day 14 NPS responses within 24 hours
- Complete handoff checklist (Section 8)

**Activation Confirmation (Day 14 EOD):**
- [ ] All 9 milestones marked Complete in tracker
- [ ] NPS score collected
- [ ] Notes added to CRM: key contacts, pain points, product feedback
- [ ] Handoff message sent to support team

---

## 7. Churn Risk Protocol

**Triggered when:** Client has completed fewer than 4 milestones by Day 8.

**Step 1 — Immediate Outreach (within 4 business hours)**
- Call the primary contact directly (use phone number from CRM)
- If no answer: leave voicemail + send personalised email
- Subject line: `Quick check-in — {{First Name}}`

**Step 2 — Diagnose the Blocker**
Use these questions on the call:
1. "Have you had a chance to log in since signing up?"
2. "Is there anything blocking you from getting started?"
3. "Would it help if I walked you through setup live — takes about 20 minutes?"

**Step 3 — Offer a Live Session**
Schedule a screen-share session. Use the live onboarding call template in `/templates/`.

**Step 4 — Escalate if No Contact by Day 10**
- Flag account as "High Churn Risk" in CRM
- Notify Senior CSM
- Senior CSM to attempt contact via LinkedIn or alternate contact

**Step 5 — Document Outcome**
- Update tracker with: contact attempts, blockers identified, resolution or churn date

---

## 8. Handoff to Support Team

Complete this checklist before closing the onboarding record:

- [ ] All milestones confirmed as Complete
- [ ] CRM notes updated with: primary contact, secondary contact, plan tier, key integrations used, any open issues
- [ ] Slack channel archived or transferred (Enterprise)
- [ ] Internal handoff email sent to support@{{company}}.com using template in `/templates/`
- [ ] Client notified of new support contact and response time SLA
- [ ] Tracker row marked "Activated" and archived

---

## 9. Escalation Matrix

| Situation | First Contact | Response Time |
|-----------|--------------|---------------|
| Client cannot log in | CSM → Support | 1 hour |
| Billing issue raised | CSM → Finance | 4 hours |
| Feature bug reported | CSM → Engineering | 2 hours |
| Legal / contract query | CSM → Legal | 24 hours |
| Client requesting cancellation | CSM → Senior CSM | Immediate |
| Data/security concern | CSM → CTO | Immediate |

---

## 10. Metrics & Reporting

**Weekly Report (sent every Monday):**
- New clients enrolled (past 7 days)
- Activation rate (% who hit all 9 milestones by Day 14)
- Average time to activation
- At-risk count
- Churn count

**Monthly Review (first Friday of month):**
- NPS trend
- Milestone bottleneck analysis (which milestone has lowest completion rate?)
- Email open rate by sequence step
- Recommendations for process improvement

---

## 11. Templates & Resources

| Resource | Location |
|----------|----------|
| Email Sequence Templates | `/templates/email-sequence.md` |
| Loom Scripts | `/templates/loom-scripts.md` |
| Milestone Tracker | `/scripts/milestone_tracker.py` |
| HubSpot Workflow | `/scripts/hubspot_workflow.json` |
| Churn Risk Checklist | `/docs/churn-risk-checklist.md` |
| Live Onboarding Call Script | `/templates/live-call-script.md` *(coming soon)* |
