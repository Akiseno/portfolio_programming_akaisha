#fizzbuzz challenge basic version
statistics = {
    "Fizz": 0,
    "Buzz": 0,
    "FizzBuzz": 0,
    "other": 0
}

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  
        statistics["FizzBuzz"] += 1
    elif i % 3 == 0:
        print("Fizz") 
        statistics["Fizz"] += 1
    elif i % 5 == 0:
        print("Buzz")
        statistics["Buzz"] += 1
    else:
        statistics["other"] += 1
        print(i)
    

print(statistics)
