import random

player_scores = [0, 0]
turn_total = 0
current_player = random.randint(0, 1)
hold_at = 20  

def print_scores():
    print("Player 1 score:", player_scores[0])
    print("Player 2 score:", player_scores[1])

def check_for_winner():
    if player_scores[current_player] >= 100:
        print("Player", current_player + 1, "wins!")
        return True
    return False

def computer_player_turn():
    global turn_total
    while True:
        roll = random.randint(1, 6)
        print("Roll:", roll)
        if roll == 1:
            turn_total = 0
            print("Turn total:", turn_total)
            print("New score:", player_scores[current_player])
            return
        else:
            turn_total += roll
            if turn_total >= hold_at or player_scores[current_player] + turn_total >= 100:
                player_scores[current_player] += turn_total
                turn_total = 0
                print("Turn total:", turn_total)
                print("New score:", player_scores[current_player])
                return

print("You will be player", current_player + 1)
print("Enter nothing to roll; enter anything to hold.")

while True:
    print_scores()
    print("It is player", current_player + 1, "'s turn.")

    if current_player == 0:
        decision = input()
        if not decision:
            roll = random.randint(1, 6)
            print("Roll:", roll)
            if roll == 1:
                turn_total = 0
                print("Turn total:", turn_total)
                print("New score:", player_scores[current_player])
                current_player = (current_player + 1) % 2
            else:
                turn_total += roll
                if check_for_winner():
                    break
                print("Turn total:", turn_total, "\tRoll/Hold?")
        else:
            player_scores[current_player] += turn_total
            turn_total = 0
            print("New score:", player_scores[current_player])
            current_player = (current_player + 1) % 2
            if check_for_winner():
                break

    else:
        computer_player_turn()
        current_player = (current_player + 1) % 2
        if check_for_winner():
            break

print_scores()

