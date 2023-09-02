"""
CP1404/CP5632 Practical 7 - Client code to use the Project  class.
Estimate: 20 minutes
Actual:   30 minutes
"""
import datetime
from prac_07.project import Project

MENU = """ 
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

FILE_NAME = 'projects.csv'


def main():
    load_projects()
    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != 'q':
        if choice == 'l':
            load_projects()
            print("Projects loaded successfully.")
        elif choice == 's':
            save_projects()
            print("Projects saved successfully.")
        elif choice == 'd':
            display_projects()
        elif choice == 'f':
            pass
        elif choice == 'a':
            add_new_project()
        elif choice == 'u':
            update_project()
        else:
            print("Invalid choice. Please select a valid option.")

    print("Thank you for using custom-built project management software.")


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects_by_date():
    pass


def add_new_project():
    pass


def update_project():
    pass


main()
