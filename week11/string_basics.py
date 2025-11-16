#string basics and operations
print("String Basics and Operations")
name = "Akaisha"
age = 10
hobby = "reading"
favorite_game = "pokemon"

print("My name is", name)
print("I am", age, "years old")
print("My hobby is", hobby)
print("My favorite game is", favorite_game)

print("the length of my name is", len(name))
print("the length of my hobby is", len(hobby))
print("the length of my favorite game is", len(favorite_game))

#finding index of a character
print(name[0])
print(str(age)[0])
print(hobby[0])
print(favorite_game[0])

#getting first 3 character of name
print(name[:3])
print(str(age)[:3])
print(hobby[:3])
print(favorite_game[:3])

#string concutination
full_name = name + " " + str(age)
print(full_name)

#repetition
print(name * 3)

