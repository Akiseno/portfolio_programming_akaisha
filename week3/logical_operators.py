#and operator
age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")






#or operator
weather = input("whats the weather: ")
if weather == "rain" or weather == "hail":
    print("Take an umbrella")
else:
    print("Enjoy the weather")






#not operator
has_license = input("Do you have a driver's license? (yes/no): ")
if not has_license == "yes":
    print("You are not eligible to drive")
else:
    print("You are eligible to drive")