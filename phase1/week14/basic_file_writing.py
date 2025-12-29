with open("output.txt", "w") as file:
    file.write ("line 1")
    file.write ("line 2")
    file.write ("line 3")
    file.write ("line 4")

poo = "kaka"
lines = ["line1\n", "line2\n", "line3\n", "line4\n"]
with open("lines.txt", "w") as file:
    file.writelines(poo)


