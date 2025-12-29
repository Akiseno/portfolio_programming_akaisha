def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_area_of_circle(radius):
    return 3.14 * radius * radius

area = calculate_area(10, 20)
perimeter = calculate_perimeter(10, 20)
area_of_circle = calculate_area_of_circle(10)

print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)
print("The area of the circle is", area_of_circle)

