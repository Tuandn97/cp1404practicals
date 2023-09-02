"""
CP1404/CP5632 Practical 7 - Client code to use the Project  class.
Estimate: 11:40
Actual:   30 minutes
"""
import datetime
from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

FILE_NAME = 'projects.txt'
NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENT_COMPLETE_INDEX = 4


def main():
    projects = load_projects(FILE_NAME)
    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_projects(FILE_NAME)
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


def load_projects(file_name):
    projects = []
    with open(file_name) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[NAME_INDEX]
            start_date = datetime.datetime.strptime(parts[DATE_INDEX].strip(), "%d/%m/%Y").date()
            priority = int(parts[PRIORITY_INDEX])
            cost_estimate = float(parts[COST_INDEX])
            percent_complete = int(parts[PERCENT_COMPLETE_INDEX])
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)
    return projects


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
