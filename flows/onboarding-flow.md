# Onboarding Journey Map — End-to-End Flow

This document maps the full customer journey from account creation to activation, including touchpoints, system actions, and CSM responsibilities at each stage.

---

## Journey Overview

```
Account Created → Day 0 Welcome → Day 1 Core Feature → Day 3 Team Invite
      ↓                                                         ↓
  HubSpot                                               Milestone Check
  Enrolled                                                     ↓
                                                    Day 5: At-Risk Detection
                                                             ↓
                                              Day 7: Check-In → Day 10: Advanced
                                                                       ↓
                                                             Day 14: Activation + NPS
                                                                       ↓
                                                              Handoff to Support
```

---

## Stage 1: Onboarding Initiated (Day 0)

**Trigger:** New account created in platform  
**Systems:** Platform DB → HubSpot (webhook) → Email Provider

| Actor | Action |
|-------|--------|
| System | Creates account, sends login credentials |
| HubSpot | Enrolls contact in onboarding workflow |
| System | Sends Day 0 welcome email (automated) |
| CSM | Personalises and reviews Day 0 send (Enterprise clients only) |

**Customer Experience:**
- Receives welcome email with login link
- Logs in for first time
- Sees product dashboard

**Success Signal:** Login recorded in platform within 24 hours

---

## Stage 2: Core Setup (Days 1–3)

**Goal:** Customer configures the core feature and understands basic navigation

| Actor | Action |
|-------|--------|
| System | Sends Day 1 email with core feature walkthrough |
| Customer | Watches Loom video, configures core feature |
| System | Sends Day 3 team invite email |
| CSM | Monitors email open rates; intervenes if Day 1 unopened by Day 2 |

**Customer Experience:**
- Receives structured guidance via email + video
- Completes first meaningful action in product
- Invites team members

**Success Signal:** Core feature configured; at least 1 login recorded by Day 3

---

## Stage 3: Team Activation (Days 4–7)

**Goal:** Team is connected; collaborative use begins

| Actor | Action |
|-------|--------|
| System | Runs at-risk detection logic (Day 5) |
| CSM | Reviews milestone tracker; flags at-risk accounts |
| System | Sends Day 7 check-in email |
| CSM | Creates follow-up task in HubSpot for Day 7 |
| Customer | Responds to check-in; books call if needed |

**Risk Detection Trigger:** < 4 milestones complete by Day 5 → CSM personal outreach

**Customer Experience:**
- Gets check-in email that feels personal, not automated
- Has clear path to get help (Calendly link)

---

## Stage 4: Advanced Unlock (Days 8–10)

**Goal:** Customer moves beyond basics into power features

| Actor | Action |
|-------|--------|
| System | Sends Day 10 advanced feature email |
| CSM | Personalises email for at-risk or high-value accounts |
| Customer | Configures advanced feature (target: 70% completion by Day 12) |

---

## Stage 5: Activation & Handoff (Days 12–14)

**Goal:** All milestones complete; NPS collected; smooth handoff to support

| Actor | Action |
|-------|--------|
| System | Sends Day 14 activation + NPS email |
| CSM | Reviews NPS response within 24 hours |
| CSM | Completes handoff checklist (see runbook Section 8) |
| CSM | Sends personal closing note to primary contact |
| System | Updates lifecycle stage to "Customer — Active" |
| Support Team | Receives handoff notification; reviews CRM notes |

**Customer Experience:**
- Receives confirmation that onboarding is complete
- Knows who their new support contact is
- Has been asked for feedback (NPS)

---

## Failure Modes & Mitigations

| Failure | Signal | Mitigation |
|---------|--------|-----------|
| Customer doesn't log in | No login by Day 2 | CSM personal email + call |
| Core feature not set up | Milestone unchecked Day 3 | Offer live setup session |
| No team invited by Day 5 | Milestone unchecked | Remind of value; offer to do it together |
| Customer stops replying | 2+ emails unopened | LinkedIn / phone outreach |
| Customer requests cancellation | Support ticket or direct email | Escalate to Senior CSM immediately |

---

## Key Metrics (Per Cohort)

Track these at Day 7 and Day 14 for every cohort:

| Metric | Day 7 Target | Day 14 Target |
|--------|-------------|--------------|
| Logged in at least once | 100% | 100% |
| Core feature configured | 85% | 95% |
| Team member invited | 65% | 85% |
| All 9 milestones complete | — | 85% |
| NPS collected | — | 80% |
