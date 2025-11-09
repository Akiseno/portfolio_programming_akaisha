#pattern1 compare all pairs
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if i != j:
            if numbers[i] > numbers[j]:
                print(numbers[i], "is greater than", numbers[j])
            elif numbers[i] < numbers[j]:
                print(numbers[i], "is less than", numbers[j])
            else:
                print(numbers[i], "is equal to", numbers[j])


# #multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("--------------------------------")






#2d grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in grid:
    for item in row:
        print(item)
    print("--------------------------------")



#list manipulation
numbers_with_duplicates = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#remove duplicates
numbers_without_duplicates = []
for number in numbers_with_duplicates:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)
print(numbers_without_duplicates)

#pattern to reverse list
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])

numbers.reverse()
print(numbers)


#find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            common_list.append(list1[i])
print(common_list)


