from users.users import register_user, login
from projects.projects import create_project, view_projects, edit_project

while True:
    print("\nMain Menu")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        user = login()
        if user:
            while True:
                print("\nProject Menu")
                print("1. Create Project")
                print("2. View All Projects")
                print("3. Edit My Project")
                print("4. Logout")

                project_choice = input("Choose an option: ")

                if project_choice == "1":
                    create_project(user.email)
                elif project_choice == "2":
                    view_projects()
                elif project_choice == "3":
                    edit_project(user.email)
                elif project_choice == "4":
                    print("\nLogging out...")
                    break
                else:
                    print("Invalid choice. Try again.")
    elif choice == "3":
        print("\nExiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
