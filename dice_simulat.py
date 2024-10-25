import random

def get_user_input():
    while True:
        user_input = input("Enther the number of your Dice(or ' quit' to stop playing):")
        if user_input.lower()=='quit':
            return None
        try:
            choice = int(user_input)
            if 1 <= choice <= 6:
                return choice
            else:
                print("Inputan salah. Enter new number!")
        except ValueError:
            print("Invalid input!")

def get_computer_choice():
    return random.randint(1,6)


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return " It's Tie!"
    elif user_choice > computer_choice:
        return "You Win!"
    else:
        return "You lose!"
    
def magic_dice():
    print("======Welcome to Magic Dice game=======")

    user_win = 0
    computer_win = 0
    ties = 0

    while True:
        user_choice = get_user_input()
        if user_choice is None:
            print("Thanks for playing!")
            break
        
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = winner(user_choice, computer_choice)
        print(result)
        
        # Update score
        if result == "You Win!":
            user_win += 1
        elif result == "You lose!":
            computer_win += 1
        else:
            ties += 1
        
        print(f"Score - You: {user_win}, Computer: {computer_win}, Ties: {ties}")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    magic_dice()




