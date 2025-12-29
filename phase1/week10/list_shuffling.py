#method1 random shuffle
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

#random sample 
numbers = [1, 2, 3, 4, 5]
sample = random.sample(numbers, 3)
print(sample)

#manual shuffling
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    j = random.randint(0, len(numbers) - 1)
    numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)


#shuffling diff data types
numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry", "date", "elderberry"]
mixed = numbers + strings
random.shuffle(mixed)
print(mixed)