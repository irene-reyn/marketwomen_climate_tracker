import csv
from collections import Counter
import matplotlib.pyplot as plt

def run_analysis():
    filename = "market_women_climate_data.csv"
    entries = []

    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["Age"] = int(row["Age"])
                row["Monthly Income (GHS)"] = float(row["Monthly Income (GHS)"])
                row["Income Affected (True/False)"] = row["Income Affected (True/False)"] == "True"
                entries.append(row)
    except FileNotFoundError:
        print("Data file not found.")
        return

    # Summary stats
    print(f"\nTotal women surveyed: {len(entries)}")

    total_income = sum(e["Monthly Income (GHS)"] for e in entries)
    average_income = total_income / len(entries)
    print(f"Average monthly income: GHS {average_income:.2f}")

    affected_count = sum(1 for e in entries if e["Income Affected (True/False)"])
    print(f"Women whose income is affected by climate: {affected_count}")

    percent_affected = (affected_count / len(entries)) * 100
    print(f"Percentage affected by climate: {percent_affected:.1f}%")

    # Climate issues
    climate_issues = [e["Climate Issue Faced"].strip().lower() for e in entries]
    issue_counts = Counter(climate_issues)

    print("\nClimate issues reported:")
    for issue, count in issue_counts.items():
        print(f"- {issue.title()}: {count} report(s)")

    # Bar chart
    issues = list(issue_counts.keys())
    counts = list(issue_counts.values())

    plt.figure(figsize=(8, 5))
    plt.bar(issues, counts, color='skyblue')
    plt.title("Climate Issues Reported by Market Women")
    plt.xlabel("Climate Issue")
    plt.ylabel("Number of Reports")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Pie chart
    labels = ["Income Affected", "Not Affected"]
    not_affected = len(entries) - affected_count
    sizes = [affected_count, not_affected]
    colors = ["#ff9999", "#99ccff"]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title("Impact of Climate on Income")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

    # Market filter
    filter_choice = input("\nDo you want to view data from a specific market? (yes/no): ").strip().lower()
    if filter_choice == "yes":
        market_name = input("Enter market name to filter: ").strip().lower()
        filtered = [e for e in entries if e["Market"].strip().lower() == market_name]

        if not filtered:
            print(f"No data found for market: {market_name}")
        else:
            print(f"\nData for market: {market_name.title()}")
            for entry in filtered:
                print(f"- {entry['Name']} | {entry['Business Type']} | GHS {entry['Monthly Income (GHS)']} | Climate Issue: {entry['Climate Issue Faced']}")
