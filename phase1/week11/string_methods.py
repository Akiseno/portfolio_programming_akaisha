#string methods 
print("String Methods")
name = "Akaisha"
age = 10
hobby = "reading"
favorite_game = "pokemon"

#case conversion
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())


#validation methods
print("--------------------------------")
test_string = "Hello", "123", "Hello123","HELLO"
for string in test_string:
    properties = []
    if string.isalpha():
        properties.append("all alphabetic")
    if string.isdigit():
        properties.append("all numeric")
    if string.isalnum() and not string.isalpha() and not string.isdigit():
        properties.append("alphanumeric")
    if string.isupper():
        properties.append("all uppercase")
    if string.islower():
        properties.append("all lowercase")
    if string.istitle():
        properties.append("title case")
    
    if properties:
        print(string, "is", " and ".join(properties))
    else:
        print(string, "is a mix of alphabetic and numeric")


#string searching and manipulation
text = "python programming is awesome"
print(text)
print(text.find("python"))
print(text.find("programming"))
print(text.find("awesome"))
print(text.count('o'))
print(text.count("ing"))
print(text.replace("awesome", "bad"))
print(text.split())
print("-".join(["python", "programming", "is", "awesome"]))



messy_text = "  This is a        messy text with extra spaces and   tabs.  "
print(messy_text)
print(messy_text.strip())
print(" ".join(messy_text.split()))
