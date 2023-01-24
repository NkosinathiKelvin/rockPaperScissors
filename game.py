import random


def game_mode():
    print("""
Greetings player,
Welcome to rock paper scissors.

Choose a game mode:
    (1) player v comp
    (2) player 1 v player 2
    (q) exit game
    """)

    while True:
        player_input = input("> ")

        if player_input.isdigit():
            player_input = int(player_input)

            if (player_input == 1) or (player_input == 2):
                return player_input

        elif player_input == 'q':
            print("Exiting game..")
            exit()

        print("""Oops!
Enter a valid choice:
    (1) player v comp
    (2) player 1 v player 2
    (q) quit
            """)


def one_player_mode():

    while True:
        # computer choice
        allocated_words = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(allocated_words)

        # player choice
        print("""
Choose an option:
    (r)ock
    (p)aper
    (s)cissors

    (q) exit game
    """)

        player_input = input("> ")

        if player_input == 'q':
            print("Exiting game..")
            exit()
        elif (player_input == 'r') or (player_input == 'rock'):
            player_choice = 'rock'
        elif (player_input == 'p') or (player_input == 'paper'):
            player_choice = 'paper'
        elif (player_input == 's') or (player_input == 'scissors'):
            player_choice = 'scissors'
        else:
            print("""Oops! Enter a valid choice,""")
            continue

        # One player mode gameplay
        if computer_choice == player_choice:
            print(f"""
Computer choice: {computer_choice}
Player choice: {player_choice}

You both chose {computer_choice},
It's a tie.
""")
        elif computer_choice == 'rock':
            if player_choice == 'paper':
                print("""
Computer choice: rock
Player choice: paper

Paper beats rock,
You win!!
""")
            elif player_choice == 'scissors':
                print("""
Computer choice: rock
Player choice: scissors

Rock beats scissors,
You lose..
""")
        elif computer_choice == 'paper':
            if player_choice == 'rock':
                print("""
Computer choice: paper
Player choice: rock

Paper beats rock,
You lose..
""")
            elif player_choice == 'scissors':
                print("""
Computer choice: paper
Player choice: scissors

Scissors beats paper,
You win!!
""")
        elif computer_choice == 'scissors':
            if player_choice == 'rock':
                print("""
Computer choice: scissors
Player choice: rock

Rock beats scissors,
You win!!
""")
            elif player_choice == 'paper':
                print("""
Computer choice: scissors
Player choice: paper

Scissors beats paper,
You lose..
""")
        print("\n--- NEW GAME ---")


def two_player_mode():

    while True:
        # player 1 choice
        print("""
Player 1:
    Choose an option:
        (r)ock
        (p)aper
        (s)cissors

        (q) exit game
    """)

        player1_input = input("> ")

        if player1_input == 'q':
            print("Exiting game..")
            exit()
        elif (player1_input == 'r') or (player1_input == 'rock'):
            player1_choice = 'rock'
        elif (player1_input == 'p') or (player1_input == 'paper'):
            player1_choice = 'paper'
        elif (player1_input == 's') or (player1_input == 'scissors'):
            player1_choice = 'scissors'
        else:
            print("""Oops! Enter a valid choice,""")
            continue

        # player 2 choice
        print("""
Player 2:
    Choose an option:
        (r)ock
        (p)aper
        (s)cissors

        (q) exit game
    """)

        player2_input = input("> ")

        if player2_input == 'q':
            print("Exiting game..")
            exit()
        elif (player2_input == 'r') or (player2_input == 'rock'):
            player2_choice = 'rock'
        elif (player2_input == 'p') or (player2_input == 'paper'):
            player2_choice = 'paper'
        elif (player2_input == 's') or (player2_input == 'scissors'):
            player2_choice = 'scissors'
        else:
            print("""Oops! Enter a valid choice,""")
            continue

        # two player mode gameplay
        if player1_choice == player2_choice:
            print(f"""
Player 1 choice: {player1_choice}
Player 2 choice: {player2_choice}

You both chose {player1_choice},
It's a tie.
""")
        elif player1_choice == 'rock':
            if player2_choice == 'paper':
                print("""
Player 1 choice: rock
Player 2 choice: paper

Paper beats rock,
Player 2 wins!!
""")
            elif player2_choice == 'scissors':
                print("""
Player 1 choice: rock
Player 2 choice: scissors

Rock beats scissors,
Player 1 wins!!
""")
        elif player1_choice == 'paper':
            if player2_choice == 'rock':
                print("""
Player 1 choice: paper
Player 2 choice: rock

Paper beats rock,
Player 1 wins!!
""")
            elif player2_choice == 'scissors':
                print("""
Player 1 choice: paper
Player 2 choice: scissors

Scissors beats paper,
Player 2 wins!!
""")
        elif player1_choice == 'scissors':
            if player2_choice == 'rock':
                print("""
Player 1 choice: scissors
Player 2 choice: rock

Rock beats scissors,
Player 2 wins!!
""")
            elif player2_choice == 'paper':
                print("""
Player 1 choice: scissors
Player 2 choice: paper

Scissors beats paper,
Player 1 wins!!
""")
        print("\n--- NEW GAME ---")


if __name__ == '__main__':
    if game_mode() == 1:
        print("Game mode: player v comp")
        one_player_mode()
    else:
        print("Game mode: player 1 v player 2")
        two_player_mode()