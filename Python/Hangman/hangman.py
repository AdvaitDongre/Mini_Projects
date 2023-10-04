import random

def word_choice():
    li = ["apple","banana","pineapple","watermelon"]
    return random.choice(li)

def display(word, guessed_letters):
    display = ""
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"
    return display
def game():
    secret_word = word_choice()
    max_attempts = len(secret_word) + 2
    guessed_letters = [] * max_attempts
    guessed_word = "_" * len(secret_word)

    print(f"Welcome to the hangman game\nYou have this many number of tries: {max_attempts}")

    while(max_attempts>0):
        print(f"your tries: {max_attempts}")
        print(display(secret_word,guessed_letters))
        guess = input("Guess a letter: ").lower()
        if len(guess)>1:
            print("Please enter a single letter")
            continue
        elif not guess.isalpha():
            print("Enter something valid")
            continue
        elif guess in guessed_letters:
            print("You have already guessed that letter")
            continue
        guessed_letters.append(guess)
        guessed_word = display(secret_word, guessed_letters)

        if guessed_word == secret_word:
            print("CONGRATTS YOU WON")

            x = input("Want to play again? (yes or no)\n")
            if x.lower()=="yes":
                game()
            else:
                break
        if max_attempts==0:
            print(f"YOU LOSE, the word was {secret_word}")
            x = input("Want to play again? (yes or no)\n")
            if x.lower()=="yes":
                game()
            else:
                break
        max_attempts -= 1
game()