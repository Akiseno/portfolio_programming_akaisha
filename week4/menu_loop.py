from datetime import datetime

choice = ""
while choice.lower() != "quit":
    print("--------------------------------")
    print("Menu")
    print("1. say hello")
    print("2. tell a joke")
    print("3. show the time")
    print("type quit to exit")
   


    choice = input("What do you want to do? ")
    if choice.lower() == "1":
        print("Hello")
    elif choice.lower() == "2":
        print("What do you call a fish with no eyes? A fsh")
    elif choice.lower() == "3":
        print("The time is", datetime.now())
    elif choice.lower() == "quit":
        print("Thank you for using the menu")
    else:
        print("Invalid choice")
print("done")  