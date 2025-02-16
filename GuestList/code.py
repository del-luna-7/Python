import os


def add(faddGuest):
    file = open("Guests.txt", "a")
    file.write(faddGuest)
    file.write(",")
    file.close()


def edit(foldGuest, fnewGuest):
    file = open("Guests.txt", "r")
    spisok = file.read().split(",")
    for i in range(len(spisok)-1):
        if spisok[i] == foldGuest:
            spisok[i] = fnewGuest
    file.close()

    spisok.remove(spisok[len(spisok) - 1])  # Удаление лишней запятой в конце списка

    os.remove(r"C:\Users\User\Desktop\pyProject\pythonProject\Guests.txt")

    file = open("Guests.txt", "a")
    for i in spisok:
        file.write(i)
        file.write(",")
    file.close()


def Delete(fdelete):
    file = open("Guests.txt", "r")
    spisok = file.read().split(",")
    for i in range(len(spisok) - 1):
        if spisok[i] == fdelete:
            spisok.remove(fdelete)
    file.close()

    spisok.remove(spisok[len(spisok) - 1])  # Удаление лишней запятой в конце списка

    os.remove(r"C:\Users\User\Desktop\pyProject\pythonProject\Guests.txt")

    file = open("Guests.txt", "a")
    for i in spisok:
        file.write(i)
        file.write(",")
    file.close()


def show():
    file = open("Guests.txt", "r")
    spisok = file.read().split(",")
    print(spisok)
    file.close()


while True:
    print("1-Add \n2-Edit \n3-Delete\n4-Show\n5-Exit")
    choice = input("Your choice: ")

    if choice == "1":
        addGuest = input("Enter guest to add: ")
        add(addGuest)

    elif choice == "2":
        oldGuest = input("Enter old guest: ")
        newGuest = input("Enter new guest: ")
        edit(oldGuest, newGuest)

    elif choice == "3":
        delete = input("Enter guest to delete: ")
        Delete(delete)

    elif choice == "4":
        show()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Error choice. Try again.")

