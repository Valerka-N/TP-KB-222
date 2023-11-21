import csv

slist = []

def printAllList(slist):
    for elem in slist:
        StrForPrint ="  Student name: " +elem["name"] + "  Phone Number: " + elem["phone"] + "  Specialty: " + elem["specialty"] + "  Group: " + elem["group"]
        print(StrForPrint)
    return

def addNewElement(slist):
    name = input("Please enter name: ")
    phone = input("Please enter phone: ")
    specialty = (input("Please enter specialty: "))
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "specialty": specialty, "group": group}

    slist.append(newItem)
    slist.sort(key=lambda student: student["name"])
    print("Element: add")

def deleteElement(slist):
    name = input("Please enter name to be deleted: ")
    for student in slist:
        if name == student["name"]:
            slist.remove(student)
            print("Element: deleted")
            break
    else:
        print("Element: not found")

def updateElement(slist):
    name = input("Please enter name to be updated: ")
    for student in slist:
        if name == student["name"]:
            student["name"] = input("Enter new name: ")
            student["specialty"] = input("Enter new specialty: ")
            student["phone"] = input("Enter new phone number: ")
            student["group"] = input("Enter new group: ")
            slist.sort(key=lambda student: student["name"])
            print("Element: updated")
            break
    else:
        print("Student not found")


def add(file, slist):
    with open(file, encoding="utf-8", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(f"Read row: {row}")
            slist.append({
                "name": row["name"],
                "phone": row["phone"],
                "specialty": row["specialty"],
                "group": row["group"],
            })
    return slist

def save(file, slist):
    try:
        with open(file, "w", newline="", encoding="utf-8") as saveFile:
            fieldnames = ["name", "phone", "specialty", "group"]
            writer = csv.DictWriter(saveFile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(slist)
        print("File saved")
    except IOError as e:
        print(f"Error saving data to {file}: {e}")

def main():
    slist = []
    while True:
        choice = input("Please specify the action \nC - Create \nU - Update \nD - Delete \nP - Print \nX - Exit \nL - Load \nS - Save \n   Enter: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(slist)
                printAllList(slist)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(slist)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(slist)
            case "P" | "p":
                print("List will be printed")
                printAllList(slist)
            case "X" | "x":
                print("Leaving...")
                break
            case "L" | "l":
                file = input("Enter CSV file name: ")
                slist = add(file,slist)
            case "S" | "s":
                file = input("Enter CSV file name: ")
                save(file, slist)

if __name__ == "__main__":
    main()
