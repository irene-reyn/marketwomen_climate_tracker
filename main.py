from data_entry import collect_and_save_data
from analyze import run_analysis

def show_menu():
    print("\nMARKET WOMEN & CLIMATE IMPACT TRACKER")
    print("1. Add new data")
    print("2. Analyze data")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1, 2 or 3): ").strip()

    if choice == "1":
        collect_and_save_data()
    elif choice == "2":
        run_analysis()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
