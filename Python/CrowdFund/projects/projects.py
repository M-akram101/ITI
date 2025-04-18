import os
import pickle
import datetime


class Project:

    def __init__(self, founder_email, title, details, target, start_date, end_date):
        self.founder_email = founder_email
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date

    def show_project_data(self):
        print(f"\nTitle: {self.title}")
        print(f"Details: {self.details}")
        print(f"Target: {self.target} EGP")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")


def load_project_data(filename="projects.pkl"):
    if not os.path.exists(filename):
        return []
    with open(filename, "rb") as file:
        return pickle.load(file)


def save_projects(projects, filename="projects.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(projects, file)


def create_project(user_email):
    print("\nCreate a New Project")

    title = input("Enter project title: ")
    details = input("Enter project details: ")

    while True:
        try:
            total_target = float(input("Enter total target amount in EGP: "))
            if total_target > 0:
                break
            print("Total target must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            years = int(input("Enter start date year"))
            months = int(input("Enter start date month"))
            days = int(input("Enter start date day"))
            start_date = datetime.date(years, months, days)

            yeare = int(input("Enter end date year"))
            monthe = int(input("Enter end date month"))
            daye = int(input("Enter end date day"))
            end_date = datetime.date(yeare, monthe, daye)

            if start_date < end_date:
                break
            print("End date has to be bigger than start date")
        except ValueError:
            print("Invalid date format")

    project = Project(user_email, title, details, total_target, start_date, end_date)
    projects = load_project_data()
    projects.append(project)
    save_projects(projects)


def view_projects():
    projects = load_project_data()
    if not projects:
        print("\nNo projects found")
        return

    print("\nAll Projects")
    for index, project in enumerate(projects, start=1):
        print(f"\nProject {index}: ")
        project.show_project_data()


def edit_project(user_email):
    projects = load_project_data()
    user_projects = [p for p in projects if p.founder_email == user_email]

    if not user_projects:
        print("\nYou have no projects to edit")
        return

    print("\nYour Projects: ")
    for index, project in enumerate(user_projects, start=1):
        print(f"{index}. {project.title}")

    try:
        choice = int(input("\nEnter the project number to edit: ")) - 1
        if choice < 0 or choice >= len(user_projects):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    project = user_projects[choice]

    project.title = (
        input("Enter new title (or press Enter to keep current): ") or project.title
    )
    project.details = (
        input("Enter new details (or press Enter to keep current): ") or project.details
    )

    while True:
        try:
            total_target = input(
                "Enter new total target (or press Enter to keep current): "
            )
            if total_target:
                project.target = float(total_target)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    save_projects(projects)
    print("\nProject updated successfully!")
