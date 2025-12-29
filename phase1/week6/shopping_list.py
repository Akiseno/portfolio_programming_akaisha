shopping_list = []


def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list")

def remove_item(item):
    shopping_list.remove(item)
    print(f"{item} has been removed from the shopping list")

def show_list():
    print("Shopping List:")
    for item in shopping_list:
        print(item)

def clear_list():
    shopping_list.clear()
    print("Shopping list has been cleared")

add_item("milk")
add_item("bread")
add_item("eggs")

show_list()

remove_item("bread")

show_list()

clear_list()
show_list()

