#accumulator pattern
""" total = 0
count = 0

while count < 5:
    input_number = int(input("Enter a number: "))
    total += input_number
    count += 1

print("your total is", total)
print("average is", total / 5) """





#sentinel pattern
total = 0
count = 0

print("Enter a number (enter -1 to quit): ")
input_number = int(input("Enter a number: ")) 
while input_number != -1:
    total += input_number
    count += 1
    input_number = int(input("Enter a number: "))


if count > 0:
    print("your total is", total)
    print("average is", total / count)
else:
    print("no numbers entered")
