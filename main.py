def main():
    print("Welcome to the Quiz Game!")

    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": 1},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"],
         "answer": 2},
        {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": 3},
    ]

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")

        while True:
            try:
                user_answer = int(input("Your answer (choose the number): "))
                if 1 <= user_answer <= len(q['options']):
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Please enter a number.")

        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}.")

    print(f"\nYou completed the quiz! Your final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    main()