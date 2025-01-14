import time
import sys

def main():
    print("Welcome to the Quiz Game!")

    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": 1},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 2},
        {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": 3},
        # Ajoute d'autres questions si nécessaire
    ]

    num_questions = min(10, len(questions))
    questions = questions[:num_questions]

    score = 0
    time_limit = 10  # Time limit in seconds

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")

        start_time = time.time()  # Start the timer
        answered = False

        while True:
            elapsed_time = time.time() - start_time
            remaining_time = time_limit - int(elapsed_time)

            if remaining_time <= 0:
                print("\nTime's up! You didn't answer in time.")
                print(f"The correct answer was: {q['options'][q['answer'] - 1]}.")
                break

            # Display countdown in the same line (10, 9, 8...)
            sys.stdout.write(f"\rTime left: {remaining_time} seconds")
            sys.stdout.flush()

            try:
                user_answer = int(input(f"\n\nYour answer (choose the number): "))
                if 1 <= user_answer <= len(q['options']):
                    if user_answer == q['answer']:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}.")
                    answered = True
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Please enter a number.")

            # If answered or time is up, exit the loop
            if answered or remaining_time <= 0:
                break

        print()  # Print a blank line to move to the next question

    print(f"\nYou completed the quiz! Your final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    main()
