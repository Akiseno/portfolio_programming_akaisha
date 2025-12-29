def read_numbers_from_file(file_name):
    numbers = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()  # remove newline
            # check if the line is a number
            if line.isdigit():
                numbers.append(int(line))
            else:
                print(f"'{line}' is not a number (it's a string)")
            
        print(numbers)

read_numbers_from_file("number.txt")

