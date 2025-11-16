#string formatting
print("String Formatting")
name = "Akaisha"
age = 10
score = 100
favorite_color = "blue"

#connecting all variables
full_info = "My name is " + name + " and I am " + str(age) + " years old and my favorite color is " + favorite_color + " and my score is " + str(score)
print(full_info)

#format method
full_info = "My name is {0} and I am {1} years old and my favorite color is {2} and my score is {3}".format(name, age, favorite_color, score)
print(full_info)

#f-strings
full_info = f"My name is {name} and I am {age} years old and my favorite color is {favorite_color} and my score is {score}"
print(full_info)


#advanced fstring formatting
print("--------------------------------")
full_info = f"My name is {name.upper()} and I am {age} years old and my favorite color is {favorite_color} and my score is {score}"
print(full_info)

full_info = f"My name is {name.lower()} and I am {age} years old and my favorite color is {favorite_color} and my score is {score}"
print(full_info)

full_info = f"My name is {name.title()} and I am {age} years old and my favorite color is {favorite_color} and my score is {score}"
print(full_info)

full_info = f"My name is {name.capitalize()} and I am {age} years old and my favorite color is {favorite_color} and my score is {score}"
print(full_info)

#add 2 decimal places to score
print(f"My score is {score:.1f}")

#add percentage to score
print(f"My score is {score:.1f}%")

#text formatting
print("--------------------------------")
text = "python programming is awesome"
print(text)
print(text.center(50))  # centers text in 50 characters width
print(text.ljust(50))   # left-aligns text in 50 characters width
print(text.rjust(50))   # right-aligns text in 50 characters width
print(text.center(50, "*"))  # centers with * as fill character
print(text.ljust(50, "*"))   # left-aligns with * as fill character
print(text.rjust(50, "*"))   # right-aligns with * as fill character


animal = "dog"
verb = "bark"
place = "park"
verb2 = "run"
verb3 = "sleep"
adjective = "happy"
story = f"""Once upon a time, there was a {animal} that 
loved to {verb} in the {place}. It would {verb2} every day 
and {verb3} at night. It was a very {adjective} {animal}."""
print(story)


#interactive string fromatting
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")
favorite_game = input("Enter your favorite game: ")
story = f"""Once upon a time, there was someone named {name} that is {age} years old and
loved the color {favorite_color} in the game of {favorite_game}."""
print(story)