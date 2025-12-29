import random
questions = [
    {
        "question": "What color is the sky?",
        "answer": "blue"
        
    },
    {
        "question": "How many legs does a cat have?",
        "answer": "four"
    },
    {
        "question": "What do we use to write?",
        "answer": "pencil"
    },
    {
        "question": "What animal says 'moo'?",
        "answer": "cow"
    },
    {
        "question": "What do we eat for breakfast?",
        "answer": "cereal"
    }
]

def ask_random_question():
    question = random.choice(questions)
    print(question["question"])
    answer = input("Enter your answer: ")
    if answer == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect!")

ask_random_question()

