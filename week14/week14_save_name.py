name = input("whats your name? ")
with open("name.txt", "w") as file:
    file.write(name.capitalize())
