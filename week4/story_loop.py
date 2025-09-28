#story builder loop
story = "Once upon a time"
keep_going = "yes"


while keep_going.lower() == "yes":
    input_story = input("Add a sentence to the story: ")
    story = story + " " + input_story
    print(story)
    keep_going = input("Do you want to keep going? (yes/no): ")



print("The story is:", story)