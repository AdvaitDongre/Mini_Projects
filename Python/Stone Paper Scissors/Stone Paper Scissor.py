# stone paper and scissor 
# 1) computer selects one randomly
# 2) user selects something
# 3) the computer compares the answers and gives the result
import random
choices = ["Stone", "Paper", "Scissor"]

computer_choices = random.choice(choices)
print(computer_choices)

def player_guess():
    player_guess = input("What is your choice?\n")
    return player_guess
player = player_guess()

def game():
    if player != choices[0] and player != choices[1] and player != choices[2]:
        print("Sorry, Invalid input")
        exit()
    else:
        if computer_choices == player:
            print("Ooo interesting, you both picked same")
        else:
             
        

            if computer_choices == "Paper":
                if player == "Stone":
                        print("Aww you lose")
                else:
                        print("Awesome you win!!!")

            elif computer_choices == "Stone":

                if player == "Paper":
                    print("Awesome you win!!!")
                else:
                    print("Damn you lost")
                    
            elif  computer_choices == "Scissor":
                if player == "Stone":
                    print("Dude you fr good at this")
                else:
                    print("You sure you can play this game?")
    i = input("Do you wanna play again\n")
    o = i()
    if o == "Yes":
        return
    else:
        print("Thank you for playing")

game()
print("made by Advait")