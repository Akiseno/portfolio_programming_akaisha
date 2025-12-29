def save_user_info(name, age, fav_color):
     with open("user_info.txt", "w") as file:
          file.write(name)
          file.write(age)
          file.write(fav_color)


save_user_info("aki\n", "3\n", "brownpoo\n")

def save_list_to_file(file_name, items):
    with open(file_name, "w") as file:
        for item in items:
            file.write(item)

fruits = ["apple\n", "orange\n", "banana\n"]

save_list_to_file("inventory.txt", fruits)