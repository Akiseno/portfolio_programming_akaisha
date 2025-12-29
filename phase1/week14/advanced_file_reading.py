def read_file_safe(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content

def processed_file_data(file_name):
    with open(file_name, "r") as file:
         content = file.readlines()
         count = len((content))
         print(count)
         return count



name = read_file_safe("sample.txt")
print(name)
read = processed_file_data("sample.txt")


