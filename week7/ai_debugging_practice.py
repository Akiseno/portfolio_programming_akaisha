def greet_user(name):
    print("hello", name)

def calculate_area(length, width):
    return length * width

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
greet_user("Alice")
area = calculate_area(5, 3)
print("The area of the rectangle is", area)
grade = get_grade(70)
print("The grade is", grade)
