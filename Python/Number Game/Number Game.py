import random

def roll():
    min_value = 1
    max_value = 6
    roll_result = random.randint(min_value, max_value)
    return roll_result

while True:
    players = input("Enter the number of players (2-5): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Enter a valid number of players (2-5).")
    else:
        print("Invalid input.")

max_score = 10
players_scores = [0 for _ in range(players)]

while True:
    for player_index in range(players):
        current_score = 0
        print(f"It's Player {player_index + 1}'s turn now")
        print(f"Your total score is: {players_scores[player_index]}\n\n")
        
        while True:
            want_roll = input("Do you want to roll? Press (y) if yes, or any key to skip: ")
            if want_roll.lower() != "y":
                break
        
            value = roll()

            if (value == 1):
                current_score = 0
                print("You rolled a one!!")
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            print(f"Your current score is: {current_score}")

        players_scores[player_index] += current_score
        print(f"Your current score is: {players_scores[player_index]}")

        if players_scores[player_index] >= max_score:
            print(f"Player {player_index + 1} has reached {max_score} or more. Player {player_index + 1} wins!")
            break

    if any(score >= max_score for score in players_scores):
        break

print("Game over!")
