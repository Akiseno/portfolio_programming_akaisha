grades = []

def add_grade(grade):
    grades.append(grade)
    print(f"{grade} has been added to the grades")

def calculate_average():
    if len(grades) == 0:
        print("No grades to calculate average")
    else:
        average = sum(grades) / len(grades)
        print(f"The average grade is {average}")
        return average

def show_grades():
    print("Grades:")
    for grade in grades:
        print(grade)
    print(grades)
    average = calculate_average()
    print(f"The average grade is", average)


def get_letter_grade(average):
   if average >= 90:
        return "A"
   elif average >= 80:
        return "B"
   elif average >= 70: 
        return "C"
   else:
        return "F"

add_grade(95)
add_grade(87)
add_grade(92)
add_grade(78)
show_grades()

average = calculate_average()
letter_grade = get_letter_grade(average)
print("The letter grade is", letter_grade)




