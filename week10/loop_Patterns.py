#loop patterns with list
numbers = [1, 2, 3, 4, 5]

#pattern 1 sum all numbers
total = 0
for number in numbers:
    total += number
print(total)

#pattern2 find largest number
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

#pattern 3 count even  numbers
even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
print(even_count)


#pattern 4 create new list squares
squares = []
for number in numbers:
    squares.append(number * number)
print(squares)


print("--------------------------------")
#string processing
words = ["apple", "banana", "cherry", "date", "elderberry", "apricot", "avocado", "blueberry", "cherry", "date", "elderberry"]


#find longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

#count words with specific length
length = 6
count = 0
for word in words:
    if len(word) == length:
        count += 1
print(count)


#create uppercase list
uppercase_words = []
for word in words:
    uppercase_words.append(word.capitalize())
print(uppercase_words)


#find words that start with a specific letter
letter = "a"
for word in words:
    if word.startswith(letter):
        print(word)