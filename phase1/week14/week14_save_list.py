with open("favorite_games.txt", "a") as file:
    while True:
        game = input("what are your favorite games? if your done then type done: ")
        favorite_games = []
        favorite_games.append((f"{game}\n"))
        if game == "done":
            break
        else:
            file.writelines(favorite_games)

            


