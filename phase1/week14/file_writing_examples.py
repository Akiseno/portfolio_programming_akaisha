from sqlite3 import SQLITE_DBCONFIG_WRITABLE_SCHEMA


def save_highscore(name, score):
    scores = []
    with open("highscores.txt", "r") as file:
        for line in file:
            line = line.strip()  # remove newline
            # check if the line is a number
            if line.isdigit():
                SQLITE_DBCONFIG_WRITABLE_SCHEMA.append(int(line))
            else:
                print(f"'{line}' is not a number (it's a string)")

