import csv

filename = "market_women_climate_data.csv"

fieldnames = [
    "Name",
    "Age",
    "Market",
    "Business Type",
    "Monthly Income (GHS)",
    "Climate Issue Faced",
    "Income Affected (True/False)",
    "Comments"
]

def collect_data():
    data = {}
    data["Name"] = input("Enter name: ")
    data["Age"] = int(input("Enter age: "))
    data["Market"] = input("Enter market name: ")
    data["Business Type"] = input("Enter business type: ")
    data["Monthly Income (GHS)"] = float(input("Enter monthly income (GHS): "))
    data["Climate Issue Faced"] = input("What climate issue affects her (e.g. flooding, heat)? ")

    affected = input("Has this affected her income? (yes/no): ").strip().lower()
    data["Income Affected (True/False)"] = True if affected == "yes" else False

    data["Comments"] = input("Any additional comments? ")

    return data

def save_to_csv(data, filename):
    try:
        with open(filename, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print("Error saving data:", e)

def collect_and_save_data():
    while True:
        entry = collect_data()
        save_to_csv(entry, filename)
        again = input("Add another entry? (yes/no): ").strip().lower()
        if again != "yes":
            print("Done collecting data.")
            break
