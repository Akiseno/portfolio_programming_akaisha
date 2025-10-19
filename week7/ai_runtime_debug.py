def broken_calculator():
    numbers = [1, 2, 3, 4, 5]
    length = len(numbers)
    print("the length of the list is", length)


    #accessing index out of range
    print(numbers[4])
    
    #math with text
    age = 20
    next_year_age = age + 1
    print("Next year you will be", next_year_age, "years old")

    #try to use undefined variable
    total = 10 + 20
    print("the total is", total)

broken_calculator()