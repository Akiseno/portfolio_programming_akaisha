password = "123456"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    guess = input("Enter the password: ")
    if guess != password:
        print("Invalid password")
    else:
        print("Welcome to the system")
        break

if attempts >= max_attempts:
    print("Too many attempts")