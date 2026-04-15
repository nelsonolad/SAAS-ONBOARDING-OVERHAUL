#!/usr/bin/env python3
"""
Onboarding Milestone Tracker Generator
Generates a CSV tracker for managing SaaS client onboarding progress.

Usage:
    python milestone_tracker.py --clients 40 --output tracker.csv
    python milestone_tracker.py --clients 10 --output my_tracker.csv --start-date 2024-01-15
"""

import argparse
import csv
import random
from datetime import datetime, timedelta


MILESTONES = [
    "Account Created",
    "Profile Completed",
    "Core Feature Configured",
    "Team Member Invited",
    "First Key Action Completed",
    "Advanced Feature Enabled",
    "Day 7 Check-in Done",
    "NPS Survey Submitted",
    "Fully Activated",
]

STATUSES = ["Not Started", "In Progress", "Complete", "Blocked"]

SAMPLE_COMPANIES = [
    "Acme Corp", "BrightPath Inc", "CloudNine Ltd", "DataFlow Co",
    "EasyOps", "FinTrack Pro", "GrowthBase", "HubWorks",
    "InnovateCo", "JetStream Solutions", "KlearView", "LaunchPad Inc",
    "MetaSync", "NorthStar Tech", "OpenLoop", "PinPoint SaaS",
    "QuickBase", "RiseUp Corp", "SkyBridge", "TrueNorth Analytics",
]

CSMS = ["Alex O.", "Sarah M.", "Daniel K.", "Priya N."]


def generate_tracker(num_clients: int, start_date: datetime) -> list[dict]:
    rows = []
    for i in range(num_clients):
        company = SAMPLE_COMPANIES[i % len(SAMPLE_COMPANIES)]
        if i >= len(SAMPLE_COMPANIES):
            company = f"{company} {i // len(SAMPLE_COMPANIES) + 1}"

        onboarding_start = start_date + timedelta(days=random.randint(0, 30))
        days_in = (datetime.now() - onboarding_start).days
        days_in = max(0, days_in)

        row = {
            "Client ID": f"CLT-{1000 + i}",
            "Company": company,
            "Primary Contact": f"contact{i}@{company.lower().replace(' ', '')}.com",
            "CSM": CSMS[i % len(CSMS)],
            "Onboarding Start": onboarding_start.strftime("%Y-%m-%d"),
            "Days In": days_in,
            "Target Activation Day": 6,
            "Actual Activation Day": random.randint(5, 14) if days_in > 6 else "",
        }

        for milestone in MILESTONES:
            if days_in == 0:
                status = "Not Started"
            elif days_in >= MILESTONES.index(milestone) * 1.5:
                status = random.choice(["Complete", "Complete", "Complete", "In Progress"])
            else:
                status = random.choice(["Not Started", "In Progress"])
            row[milestone] = status

        completed = sum(1 for m in MILESTONES if row[m] == "Complete")
        row["Milestones Completed"] = f"{completed}/{len(MILESTONES)}"
        row["Completion %"] = f"{round((completed / len(MILESTONES)) * 100)}%"

        if completed == len(MILESTONES):
            row["Status"] = "Activated"
        elif days_in > 10 and completed < 4:
            row["Status"] = "At Risk"
        elif days_in > 14 and completed < 7:
            row["Status"] = "Churned"
        else:
            row["Status"] = "On Track"

        rows.append(row)

    return rows


def write_csv(rows: list[dict], output_path: str) -> None:
    if not rows:
        print("No data to write.")
        return

    fieldnames = list(rows[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Tracker written to: {output_path}")
    print(f"Total clients: {len(rows)}")

    statuses = {}
    for row in rows:
        s = row["Status"]
        statuses[s] = statuses.get(s, 0) + 1

    print("\nStatus summary:")
    for status, count in sorted(statuses.items()):
        pct = round((count / len(rows)) * 100)
        print(f"  {status:<12} {count:>3} clients ({pct}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a SaaS onboarding milestone tracker CSV"
    )
    parser.add_argument(
        "--clients", type=int, default=40,
        help="Number of client rows to generate (default: 40)"
    )
    parser.add_argument(
        "--output", type=str, default="onboarding_tracker.csv",
        help="Output CSV filename (default: onboarding_tracker.csv)"
    )
    parser.add_argument(
        "--start-date", type=str, default=None,
        help="Cohort start date YYYY-MM-DD (default: 60 days ago)"
    )

    args = parser.parse_args()

    if args.start_date:
        start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    else:
        start_date = datetime.now() - timedelta(days=60)

    rows = generate_tracker(args.clients, start_date)
    write_csv(rows, args.output)


if __name__ == "__main__":
    main()
