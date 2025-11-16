def processed_text(text):
    print("Processing text...")
    print("Text:", text)
    print("Text has this amount of characters: ", len(text))
    print("Text has this amount of words: ", len(text.split()))
    print("The first word of this Text is: ", text.split()[0])
    print("The last word of this Text is: ", text.split()[-1])
    print("The text in uppercase is: ", text.upper())
    print("The text in lowercase is: ", text.lower())
    print("The text in title case is: ", text.title())
    print("The text in sentence case is: ", text.capitalize())

text = "Hello, World!"
processed_text(text)


#string analysis
def analyze_text(text):
    print("Analyzing text...")
    print("Text:", text)
    stats = {}
    stats["length"] = len(text)
    stats["words"] = len(text.split())
    stats["first_word"] = text.split()[0]
    stats["last_word"] = text.split()[-1]
    stats["uppercase"] = text.upper()
    stats["lowercase"] = text.lower()
    stats["title"] = text.title()
    stats["capitalize"] = text.capitalize()
    return stats

text = "Hello, World!"
stats = analyze_text(text)
print(stats)
print(stats["title"])