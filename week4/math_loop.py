import random
score = 0
question = 0
keep_going = "yes"


while keep_going.lower() == "yes":
    #generate random numbers
    num1 = random.randint(1, 10) 
    num2 = random.randint(1, 10)
    print(f"What is the sum of {num1} and {num2}: ")

    #ask question
    answer = int(input(":"))
    if answer == num1 + num2:
        print("Correct!")
        score += 1
        question += 1
        print(f"You scored {score} out of {question} questions")
    else:
        print("Incorrect!")
        question += 1
    keep_going = input("Do you want to keep going? (yes/no): ")

print(f"You scored {score} out of {question} questions")