import random

choices = ['Pedra', 'Papel', 'Tesoura']
computer = random.choice(choices)
player = None
player_name = input(
    "What's your name? (Your name must contain 8 characters)\n")

while player_name.isspace() == True:
    print("\033[4;31mERROR! Needs to contain letters!\033[m\n")
    player_name = input("What's your name? ").title()
    break

while not len(player_name) == 8:
    print("\033[4;31mERROR! Your name must contain 8 characters!\033[m\n")
    player_name = input("What's your name? ").title()

print("\033[4;32maccepted name\033[m\n")

while True:
    while player not in choices:
        player = input('pedra, papel ou tesoura? ').title()

    if player == computer:
        print(f"{player_name}: {player}")
        print('Computer: ', computer)
        print('\033[1;30;43mTie!\033[m')

    elif player == 'Pedra':
        if computer == 'Tesoura':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[30;42mYou Win!\033[m')

        if computer == 'Papel':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[1;30;41mYou lose!\033[m')

    elif player == 'Tesoura':
        if computer == 'Pedra':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[1;30;41mYou lose!\033[m')

        if computer == 'Papel':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[30;42mYou Win!\033[m')

    elif player == 'Papel':
        if computer == 'Tesoura':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[1;30;41mYou lose!\033[m')

        if computer == 'Pedra':
            print(f"{player_name}: {player}")
            print('Computer: ', computer)
            print('\033[30;42mYou Win!\033[m')

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != 'yes':
        break
    else:
        player = ''

print("Bye")
