# Churn Risk Detection Checklist

Use this checklist at Day 5, Day 8, and Day 12 of every onboarding to identify clients at risk of churning before they cancel.

---

## Early Warning Signals

Score each signal below. Total score ≥ 3 = flag as At Risk. Total score ≥ 5 = flag as High Risk.

### Engagement Signals
- [ ] Zero logins in last 48 hours — **+1**
- [ ] Zero logins since account creation — **+3**
- [ ] Day 0 welcome email unopened — **+1**
- [ ] 3+ emails in sequence unopened — **+2**
- [ ] Loom video(s) unwatched — **+1**

### Milestone Signals
- [ ] Core feature not configured by Day 3 — **+2**
- [ ] No team members invited by Day 5 — **+1**
- [ ] Fewer than 4 milestones complete by Day 8 — **+2**
- [ ] No meaningful action in product by Day 7 — **+2**

### Communication Signals
- [ ] No reply to Day 7 check-in email — **+1**
- [ ] Bounced or invalid email address — **+2**
- [ ] Client expressed frustration in a support ticket — **+2**
- [ ] Client asked about cancellation/refund — **+5**

---

## Risk Levels & Actions

| Score | Risk Level | Required Action |
|-------|-----------|-----------------|
| 0–2 | Low | Continue standard sequence |
| 3–4 | At Risk | Personal outreach within 24 hours |
| 5–7 | High Risk | Personal outreach within 4 hours + Senior CSM loop-in |
| 8+ | Critical | Immediate call + escalation to Senior CSM |

---

## Outreach Script (At Risk — Phone/Email)

**Email subject:** Quick check-in on your {{Product Name}} account

> Hi {{First Name}},
>
> I noticed you haven't had a chance to get fully set up yet — totally normal, everyone's busy.
>
> I'd love to spend 20 minutes with you on a screen share to get everything configured so you're not starting from scratch each time you log in.
>
> Would any of these times work this week?  
> → {{Calendly Link}}
>
> If now's not a great time for {{Product Name}}, just let me know — happy to pause your account or explore other options.
>
> {{CSM Name}}

---

## Resolution Outcomes

After outreach, log one of the following in the tracker:

- `Recovered` — Client re-engaged and resumed onboarding
- `Extended` — Client requested more time; onboarding extended by N days
- `Paused` — Client requested account pause (set reminder for 30 days)
- `Cancelled` — Client churned; complete exit survey if possible
- `No Contact` — Unable to reach client after 3 attempts; flag for Senior CSM

---

## Exit Survey Questions (Churned Clients)

Send via email within 24 hours of cancellation:

1. What was the main reason you decided not to continue?
2. Was there a specific feature or capability you needed that we didn't have?
3. Is there anything we could have done differently during onboarding?
4. Would you consider returning in the future if your needs change?

Record responses in CRM under the contact record tagged `churn_reason`.
