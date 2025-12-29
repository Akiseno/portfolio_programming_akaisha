import random

print("🎮 Welcome to the scoring guessing game!")
print("🤔 I am thinking of a number between 1 and 20")

#secret number
secret_number = random.randint(1, 20)
score = 100

# Keep playing until score reaches 0 or player wins
while score > 0:
    guess = int(input(f"🎯 Enter your guess (Score: {score}): "))
    
    # Check if guess is correct
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        print("💯 You scored", score, "points ✅")
        break
    elif guess < secret_number:
        print("📉 Too low! You guessed", guess, "🔄 Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("💯 You scored", score, "points ✅")
    else:
        print("📈 Too high! You guessed", guess, "🔄 Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("💯 You scored", score, "points ✅")
    
    # Check if score reached 0
    if score <= 0:
        print("💀 Game over! You ran out of points!")
        print("The secret number was:", secret_number)