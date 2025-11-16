import random
#string games
def word_scrambler(word):
    return ''.join(random.sample(word, len(word)))
word = "Akaisha"
print(word_scrambler(word))

def palendrome_checker(word):
    # A palindrome reads the same forwards and backwards
    # word[::-1] reverses the string
    return word.lower() == word[::-1].lower()  # .lower() makes it case-insensitive

# Test with different words
print("Palindrome Checker:")
print("-------------------")
test_words = ["Akaisha", "racecar", "madam", "level", "hello", "radar", "python"]
for word in test_words:
    result = palendrome_checker(word)
    status = "✓ IS a palindrome" if result else "✗ NOT a palindrome"
    print(f"'{word}' -> {status}")
    print(f"  Forwards: {word}")
    print(f"  Backwards: {word[::-1]}")
    print()
    

def word_counter(words):
    word_list = words.split()  # split the string into a list of words
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

words = "Akaisha is a amazing person"
print(word_counter(words))


#acronym generator
def acronym_generator(words):
    words = words.split()
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym

words = "Akaisha is a amazing person"
print(acronym_generator(words))