#nested list
class_grades = [["John", 85, 67, 90], ["Jane", 90, 85, 95], ["Jim", 78, 80, 85], ["Jill", 88, 90, 92]]
for student in class_grades:
    name = student[0]
    grade1 = student[1]
    grade2 = student[2]
    grade3 = student[3]
    average = (grade1 + grade2 + grade3) / 3
    print(name, "has an average grade of", average)

#printing janes first 2 grades
print(class_grades[1][1:3])

print(class_grades[3][3:])


#shopping list
shopping_list = [["apple", 5, 3.99], ["banana", 10, 1.99], ["cherry", 15, 2.99]]
total_price = 0
for item in shopping_list:
    name = item[0]
    quantity = item[1]
    price = item[2]
    total = quantity * price
    print(name, "has a total price of", total)
    total_price += total
    print("The total price of the shopping list is", total_price)