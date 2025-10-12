#basic list operations
favorite_colors = ["red", "blue", "green"]
scores = [100, 90, 80, 70, 60]
friends = ["John", "Jane", "Jim", "Jill"]

print(favorite_colors)
print(scores)
print(friends)


#index 0 first postitom
print(favorite_colors[0])
print(favorite_colors[2])
print(friends[-1])


#adding items
favorite_colors.append("yellow")
favorite_colors.insert(1, "black")
print(favorite_colors)

#list information
print(len(favorite_colors))

#check if item is in list
print("red" in favorite_colors)
print("red" not in favorite_colors)

#find position of item
print(favorite_colors.index("black"))

