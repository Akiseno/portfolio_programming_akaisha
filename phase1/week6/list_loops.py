favorite_colors = ["red", "blue", "green"]
scores = [100, 90, 80, 70, 60]

for color in favorite_colors:
    print(color)

for score in scores:
    print(score)
  
  
#list modification
favorite_colors.remove("red")
favorite_colors.insert(0, "pink")
print(favorite_colors)

favorite_colors[0] = "orange"
print(favorite_colors)

favorite_colors.pop(1)
print(favorite_colors)


