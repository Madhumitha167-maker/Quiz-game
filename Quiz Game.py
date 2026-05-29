questions = [
    {
        "question": "Capital of India?",
        "options": ["A. Chennai", "B. Delhi", "C. Mumbai"],
        "answer": "B"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nYour final score is:", score)
