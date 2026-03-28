import os

FILE_NAME = "database.txt"


def add_blocker():
    """Create (Append) a new blocker"""
    blocker = input("Enter your daily blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print("Blocker saved successfully.\n")


def fetch_blockers():
    """Read all blockers"""
    if not os.path.exists(FILE_NAME):
        print("Warning: Database file does not exist.\n")
        return

    with open(FILE_NAME, "r") as file:
        blockers = file.readlines()

    if not blockers:
        print("No blockers found.\n")
        return

    print("\n--- Team Daily Blockers ---")
    for i, blocker in enumerate(blockers, start=1):
        print(f"{i}. {blocker.strip()}")
    print()


def overwrite_warning():
    """Warn before overwriting file"""
    if not os.path.exists(FILE_NAME):
        print("No file to overwrite.\n")
        return

    confirm = input("Warning: This will overwrite all data. Continue? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")
        print("File overwritten successfully.\n")
    else:
        print("Operation cancelled.\n")


def menu():
    while True:
        print("=== TEAM DAILY STATUS SYSTEM ===")
        print("1. Add Blocker")
        print("2. Fetch Blockers")
        print("3. Overwrite File")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_warning()
        elif option == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid option.\n")


menu()

# ENGLISH PRACTICE SECTION

"""
Protocol Selection (3-C Rule):

1. I will reach out to the team via Slack because the issue is an immediate blocker and requires quick attention.
2. I would use Email if the problem needs a detailed explanation and formal documentation.
3. I would create a Jira ticket to track the issue and ensure proper follow-up within the development workflow.


Vocabulary Integration:

This script demonstrates persistence by storing data in a text file that remains available after the program ends. 
The system allows users to fetch stored blockers efficiently and review them in the console. 
It also includes an overwrite feature, which warns the user before replacing existing data. 
If any issue occurs, the user can reach out to the team using appropriate communication channels.
"""