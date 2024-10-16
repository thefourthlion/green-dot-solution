import random

def game():
    choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choices)
    player = input("Enter your choice (Rock, Paper, Scissors): ")

    print(f"\nComputer selected {computer} \nPlayer selected {player}")

    if player == computer:
        return print('Tie!')
    if player == 'Rock':
        if computer == 'Paper':
            return print('You lose!', computer, 'covers', player)
        else:
            return print('You win!', player, 'smashes', computer)
    if player == 'Paper':
        if computer == 'Scissors':
            return print('You lose!', computer, 'cut', player)
        else:
            return print('You win!', player, 'covers', computer)
    if player == 'Scissors':
        if computer == 'Rock':
            return print('You lose...', computer, 'smashes', player)
        else:
            return print('You win!', player, 'cut', computer)

def main():
    while True:
        game()

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

main()