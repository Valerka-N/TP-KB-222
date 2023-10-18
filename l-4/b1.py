import random

def get_user_choice():
    while True:
        u_choice = input("Choose: stone(st), scissors(sc), paper(p): ").lower()
        if u_choice in ['st', 'sc', 'p']:
            return u_choice
        else:
            print("Try again.")

def get_computer_choice():
    return random.choice(['st', 'sc', 'p'])

def determine_winner(u_choice, c_choice):
    win = {
        ('st', 'sc'): "You have won!",
        ('sc', 'p'): "You have won!",
        ('p', 'st'): "You have won!",
    }

    if u_choice == c_choice:
        return "Draw"
    
    if (u_choice, c_choice) in win:
        return win[(u_choice, c_choice)]

    return "The computer won."

while True:
    u_choice = get_user_choice()
    c_choice = get_computer_choice()
    print(f"Your choice: {u_choice}")
    print(f"Choosing a computer: {c_choice}")
    r = determine_winner(u_choice, c_choice)
    print(r)

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != 'y':
        break
