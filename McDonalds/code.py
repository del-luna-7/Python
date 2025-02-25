check = True

while check:
    print("\tWelcome Mac\nBurgers\nDrinks\nSouses\nExit")
    choice = input("Your choice: ")

    if choice == "Exit":
        check = False

    elif choice == "Burgers":
        lvlBurgers = True
        while lvlBurgers:
            print("BigMac\nBigTasty\nMacChicken\nBack")
            choiceBurgers = input("Your choice: ")
            if choiceBurgers == "BigMac":
                print("Big mac 10 azn")
            elif choiceBurgers == "BigTasty":
                print("Big tasty 12 azn")
            elif choiceBurgers == "MacChicken":
                print("MacChicken 15 azn")
            elif choiceBurgers == "Back":
                lvlBurgers = False
            else:
                print("Error choice! Try Again!!!! ")

    elif choice == "Drinks":
        lvlDrinks = True
        while lvlDrinks:
            print("Cola\nFanta\nSprite\nBack")
            choiceDrinks = input("Your choice: ")
            if choiceDrinks == "Cola":
                print("Cola 2.5 azn")
            elif choiceDrinks == "Fanta":
                print("Fanta 1.5 azn")
            elif choiceDrinks == "Sprite":
                print("Sprite 2 azn")
            elif choiceDrinks == "Back":
                lvlDrinks = False
            else:
                print("Error choice! Try Again!!!! ")

    elif choice == "Souses":
        lvlSouses = True
        while lvlSouses:
            print("Ketchup\nCheeseSous\nBack")
            choiceSouse = input("Your choice: ")
            if choiceSouse == "Ketchup":
                print("Ketchup 2.5 azn")
            elif choiceSouse == "CheeseSous":
                print("CheeseSous 1.5 azn")
            elif choiceSouse == "Back":
                lvlSouses = False
            else:
                print("Error choice! Try Again!!!! ")

    else:
        print("Error choice! Try Again!!!! ")


