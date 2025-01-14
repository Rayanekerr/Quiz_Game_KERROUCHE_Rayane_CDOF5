import time
import sys

def main():
    # Affiche un message de bienvenue au joueur
    print("Welcome to the Quiz Game!")

    # Liste des questions du quiz. Chaque question est un dictionnaire avec une question, des options et la réponse correcte.
    questions = <
    # Questions déjà existantes
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": 1},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 2},
    {"question": "What is 5 + 7?", "options": ["10", "11", "12", "13"], "answer": 3},
    
    # Nouvelles questions avec différentes difficultés
    # Facile
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 4},
    
    # Moyenne
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Ozone", "Oxygenium"], "answer": 1},
    
    # Difficile
    {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Homer"], "answer": 2},
    
    # Facile
    {"question": "Which animal is known as the King of the Jungle?", "options": ["Elephant", "Lion", "Tiger", "Bear"], "answer": 2},
    
    # Moyenne
    {"question": "What is the square root of 81?", "options": ["7", "8", "9", "10"], "answer": 3}

>

    # Limite le nombre de questions à 10 ou au nombre total de questions disponibles, selon ce qui est plus petit
    num_questions = min(10, len(questions))
    questions = questions[:num_questions]  # Sélectionne les premières n questions

    score = 0  # Initialisation du score à 0
    time_limit = 10  # Temps limite pour chaque question (en secondes)

    # Parcours chaque question de la liste
    for i, q in enumerate(questions):
        # Affiche la question et ses options
        print(f"\nQuestion {i + 1}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")

        # Démarre un chronomètre pour chaque question
        start_time = time.time()
        answered = False  # Variable pour vérifier si la question a été répondue

        while True:
            # Calcule le temps écoulé depuis le début
            elapsed_time = time.time() - start_time
            remaining_time = time_limit - int(elapsed_time)  # Temps restant pour répondre à la question

            # Si le temps est écoulé, affiche un message et passe à la question suivante
            if remaining_time <= 0:
                print("\nTime's up! You didn't answer in time.")
                print(f"The correct answer was: {q['options'][q['answer'] - 1]}.")
                break

            # Affiche un compte à rebours dynamique dans la même ligne
            sys.stdout.write(f"\rTime left: {remaining_time} seconds")
            sys.stdout.flush()

            try:
                # Demande la réponse à l'utilisateur
                user_answer = int(input(f"\n\nYour answer (choose the number): "))
                # Vérifie si la réponse est dans les options valides
                if 1 <= user_answer <= len(q['options']):
                    if user_answer == q['answer']:
                        print("Correct!")
                        score += 1  # Augmente le score si la réponse est correcte
                    else:
                        print(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}.")
                    answered = True  # Marque que la question a été répondue
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                # Gère les erreurs de saisie (par exemple, si l'utilisateur entre autre chose qu'un nombre)
                print("Please enter a number.")

            # Si la question a été répondue ou que le temps est écoulé, on sort de la boucle
            if answered or remaining_time <= 0:
                break

        print()  # Affiche une ligne vide pour séparer les questions

    # Affiche le score final du joueur à la fin du quiz
    print(f"\nYou completed the quiz! Your final score is {score}/{len(questions)}.")
    congratulate(score, len(questions))  # Appel de la fonction pour afficher un message de félicitations

def congratulate(score, total):
    """Affiche un message de félicitations basé sur le score"""
    if score == total:
        print("Excellent! You answered all questions correctly!")
    elif score >= total * 0.7:
        print("Well done! You did great!")
    elif score >= total * 0.5:
        print("Not bad! But you can do better!")
    else:
        print("Better luck next time! Keep trying!")

# Si ce fichier est exécuté directement, on appelle la fonction main() pour lancer le jeu
if __name__ == "__main__":
    main()
