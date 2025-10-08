def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(11))


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    
print(get_grade(90))
print(get_grade(80))
print(get_grade(70))
print(get_grade(60))