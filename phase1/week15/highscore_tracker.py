print("HIGHSCORE TRACKER")
#Akaisha:1000
scores_file = "highscores.txt"
def load_scores():
    scores = []
    with open(scores_file, "r") as file:
        for line in file:
            line = line.strip()  # remove newline
            if ":" in line:
                stat = line.split(":",1)
                score = stat[1]
                name = stat[0]
                scores.append((name, score))
                print(stat)
                print(score)
                print(scores)
        return scores
                
def save_score(scores):
    with open(scores_file, "w") as file:
        for name, score in scores:
            file.write(f"{name}:{score}\n")

def display_scores(scores):
    if not scores:
        print("No scores yet")
        return
    # sort scores from highest to lowest, converting score to int for correct order
    sorted_scores = sorted(scores, key=lambda item: int(item[1]), reverse=True)
    print("\n=== HIGHSCORES ===")
    for position, (name, score) in enumerate(sorted_scores, start=1):
        print(f"{position}. {name} - {score}")



def add_score(scores):
    while True:
        player_name = input("Enter player name: ")
        if player_name:
            break
    # keep asking until user enters a valid non-negative number
    while True:
        entered_score_str = input("Enter your SCORE: ")
        try:
            entered_score = int(entered_score_str)
            if entered_score < 0:
                print("Score cannot be negative")
            else:
                break
        except ValueError:
            print("Sorry, you need to enter a number (e.g. 1000).")
    scores.append((player_name, entered_score))
    save_score(scores)

def clear_scores(scores):
    clear = input("Would you like to delete scores?: ")
    if clear == "yes".lower():
        with open(scores_file, "w") as file:
            file.write("")

def search_player(scores, player_name):
    for name, score in scores:
        if player_name == name:
            print(score)
            return score
        else:
            print(f"{player_name} was not found")

    

   
scores = load_scores()
while True:
    print("----------------------------------------------")
    print("1.view score")
    print("2.add score")
    print("3.clear score")
    print("4.exit")
    print("5.search player")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_scores(scores)
    elif choice == "2":
        add_score(scores)
    elif choice == "3":
        clear_scores(scores)
    elif choice == "4":
        print("Goodbye")
        break
    elif choice == "5":
        searched_name = input("Who would you like to search?:  ")
        search_player(scores, searched_name)
    else:
        print("Please enter a valid choice")


    



