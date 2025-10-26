def animate_wave():
    import time
    import os
    
    waves = [
        "~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
        " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
        "  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
        "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ",
        " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
        "  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~",
    ]
    
    i = 0
    position = 0
    while True:
        os.system('clear')  # Clear screen (use 'cls' on Windows)
        print("\n" * 2)  # Move down a bit
        
        # Shark fin
        fin = "  " * position + "     /\ "
        print(fin)
        print("  " * position + "    /  \    ")
        
        print("\n" + "  " + waves[i])
        print("  " + waves[i])
        print("  " + waves[i])
        print("  " + waves[i])
        print("  " + waves[i])
        time.sleep(0.5)
        i = (i + 1) % 4  # Cycle through 0-3 infinitely
        position = (position + 1) % 5  # Move fin across

# Call the function to see the animation
animate_wave()