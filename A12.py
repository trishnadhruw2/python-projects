import random

def determine_winner(h_choice, c_choice):
    if h_choice == c_choice:
        return "It's a tie!"
    elif (h_choice == 'rock' and c_choice == 'scissors') or \
         (h_choice == 'paper' and c_choice == 'rock') or \
         (h_choice == 'scissors' and c_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    count_h = 0
    count_c = 0
    keep_playing = True

    while keep_playing:
        print("Rock, Paper, Scissors - Shoot!")
        h_choice = random.choice(['rock', 'paper', 'scissors'])
        c_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"You chose: {h_choice}")
        print(f"Computer chose: {c_choice}")

        result = determine_winner(h_choice, c_choice)
        print(result)

        if result == "You win!":
            count_h += 1
        elif result == "Computer wins!":
            count_c += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            keep_playing = False

    print(f"Final Scores - You: {count_h}, Computer: {count_c}")
    if count_h > count_c:
        print("You are the overall winner!")
    elif count_c > count_h:
        print("Computer is the overall winner!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    play_game()