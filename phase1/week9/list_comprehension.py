#basic list comprehesnion
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x*x for x in numbers]
print(squared_numbers)

sum_numbers = [x+x for x in numbers]
print(sum_numbers)

doubled_numbers = [x*2 for x in numbers]
print(doubled_numbers)

words = ["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = [len(word) for word in words]
print(word_lengths)

#change all first letters to capital
capital_words = [word.capitalize() for word in words]
print(capital_words)

#making ALL letters capital
capital_words = [word.upper() for word in words]
print(capital_words)

names = ["John", "Jane", "Jim", "Jill"]
greetings = ["Hello, " + name for name in names]
print(greetings)

