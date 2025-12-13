import random
#Phase 1 skills review checklist
#Skill 1: variables and data types
name = "Akaisha"  #string data type
age = 10 #integer data type
height = 3.5 #float data type
is_student = True #boolean data type

print(name)
print(age)
print(height)
print(is_student)


#Skill2: input and output
favorite_color = input("Enter your favorite color: ")
print("Your favorite color is", favorite_color)


#skill3: conditions
score = 85
if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
else:
    print("You got an D")

#skill4: loops
for i in range(1, 6):
    print(i)
print("done")


#skill5: functions
def greet(name):
    print("Hello", name)
greet("Akaisha")


#skill6: lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(len(fruits))

#skill7: loops with lists
for fruit in fruits:
    print(fruit)
print("done")

#skill8: strings
text = "Python programming"
print(text)
print(text.upper())
print(len(text))


#skill9: numbers
num1 = random.randint(1, 10)
print(num1)


#skill10: combining concepts
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))

