age = -1
while age < 0 or age > 120: 
    age = int(input("Enter your age: "))


    if age < 0:
        print("Age cannot be negative")
    elif age > 120:
        print("Age cannot be greater than 120")


print("Thank you for entering your age", age)




