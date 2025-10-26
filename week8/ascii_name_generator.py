def ascii_name_generator():
    name = input("Enter your name: ")
    
    # Calculate frame width: "| Name: " (8) + name + " |" (2) = 10 + len(name)
    frame_width = 10 + len(name)
    
    print("+" + "-" * (frame_width - 2) + "+")
    print("| Name: " + name + " |")
    print("+" + "-" * (frame_width - 2) + "+")

ascii_name_generator()


