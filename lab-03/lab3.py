from grup import GroupList
from flm import FileManager
from stud import Student
import os

def main():
    file_name = input("Enter CSV file name (e.g., lab-03/lab3.csv): ")
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    group_list = GroupList()
    FileManager.load_and_sort_data(file_path, group_list)
    
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()

        actions = {
            'c': lambda: group_list.add_student(Student(
        input("Please enter student name: "),
        input("Please enter student phone: "),
        input("Please enter specialty: "),
        input("Please enter group: ")
    )),
            'u': lambda: group_list.update_student(input("Please enter name to be updated: ")),
            'd': lambda: group_list.delete_student(input("Please enter name to be deleted: ")),
            'p': lambda: group_list.print_all_students(),
            'x': lambda: FileManager.save_data_to_csv(file_name, group_list) or exit(0)
        }

        chosen_action = actions.get(choice, lambda: print("Wrong choice"))
        chosen_action()

if __name__ == "__main__":
    main()
