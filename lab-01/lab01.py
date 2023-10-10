# already sorted list
list = [
    {"name": "Bob", "phone": "0631234567", "specialty": "125", "group": "kb-222"},
    {"name": "Emma", "phone": "0631234567", "specialty": "123", "group": "ce-123"},
    {"name": "Jon", "phone": "0631234567", "specialty": "121", "group": "se-211"},
    {"name": "Zak", "phone": "0631234567", "specialty": "112", "group": "st-202"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"]+ \
                      ", Specialty is " + elem["specialty"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    specialty = input("Please enter specialty: ")
    group = input("Please enter group: ")
    newItem = {"name": name, "phone": phone, "specialty": specialty, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        list.pop(deletePosition)
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            print("Select field to update:")
            print("1. Phone")
            print("2. Specialty")
            print("3. Group")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                item["phone"] = input("Enter new phone number: ")
            elif choice == "2":
                item["specialty"] = input("Enter new specialty value: ")
            elif choice == "3":
                item["group"] = input("Enter new group value: ")
            else:
                print("Invalid choice")
            print("Student information has been updated")
            return
    print("Student not found")
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()
    