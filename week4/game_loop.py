import random
score = 0
play_again = "yes"

while play_again.lower() == "yes":
    
   secret_number = random.randint(1, 10)
   guess = int(input("Enter your guess: "))

   if guess == secret_number:
       print("Correct!")
       score += 10
   else:
       print("Incorrect! the secret number is", secret_number)

   print("Your score is", score)
   play_again = input("Do you want to play again? (yes/no): ")
 
print("Thank you for playing!")
print("Your final score is", score)