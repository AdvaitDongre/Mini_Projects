import time

class Game:
    def __init__(self):
        self.tries = 0

    def ask_question(self, question, options):
        print(question)
        time.sleep(2)
        for i, option in enumerate(options, start=1):
            print(f"{chr(96+i)}) {option}")
            time.sleep(1)

    def check_answer(self, correct_option, user_answer):
        if correct_option == user_answer:
            self.tries += 1

def main():
    print("Welcome to the Better KBC\nMade by Advait\n")
    time.sleep(2)
    print("I hope you score well. Let's start!\n")
    time.sleep(2)

    game = Game()

    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Delhi", "Maharashtra", "Chennai", "Tamil Nadu"],
            "correct_option": "a"
        },
        {
            "question": "What is my name?",
            "options": ["Adi", "Advait", "Aashu", "Idk"],
            "correct_option": "b"
        }
        
    ]

    for question_data in questions:
        game.ask_question(question_data["question"], question_data["options"])
        user_answer = input("What is your answer? ").strip().lower()
        while user_answer not in ["a", "b", "c", "d"]:
            print("Sorry, invalid input. Please try again.")
            user_answer = input("What is your answer? ").strip().lower()
        game.check_answer(question_data["correct_option"], user_answer)

    print(f"You have scored {game.tries} points.")

if __name__ == "__main__":
    main()
