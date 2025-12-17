print ("Basic file reading")
#creating file
with open("sample.txt", "w") as file:
    file.write("Hello world\n")
    file.write("lololol\n")
    file.write("yaaayayayyay\n")

#reading whole file
with open("sample.txt", "r") as file:
     content = file.read()
     print(content)

#reading line by line
with open("sample.txt", "r") as file:
     line_1 = file.readline()
     line_2 = file.readline()
     line_3 = file.readline()
     print(line_1)
     print(line_2)
     print(line_3)

#reading all lines
with open("sample.txt", "r") as file:
     content = file.readlines()
     print(content)


