print("List Methods Practice")

#starting list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruits)

#adding items
fruits.append("fig")
print("After appending 'fig':", fruits)

#inserting items
fruits.insert(1, "coconut")
print("After inserting 'coconut' at index 1:", fruits)

#extending list
more_fruits = ["grape", "honeydew", "kiwi", "apple"]
fruits.extend(more_fruits)
print("After extending with more fruits:", fruits)

#removing items by index
fruits.pop(1)
print("After removing item at index 1:", fruits)

#finding index of item
index = fruits.index("cherry")
print("Index of 'cherry':", index)


#counting itmes
count = fruits.count("apple")
print("Count of 'apple':", count)

#check if item is in list
print("Is 'apple' in the list?", "apple" in fruits)
print("Is 'pear' in the list?", "pear" in fruits)

#orginizing list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print("Sorted list:", numbers)

#reversing list
numbers.reverse()
print("Reversed list:", numbers)

#sorting strings
names = ["John", "Jane", "Jim", "Jill"]
names.sort()
print("Sorted list:", names)

names.reverse()
print("Reversed list:", names)





