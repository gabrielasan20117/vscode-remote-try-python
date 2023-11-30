#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

def play():
    rounds = 0
    player1_wins = 0
    player2_wins = 0

    while True:
        player1 = input("Enter rock, paper, or scissors: ")
        player2 = input("Enter rock, paper, or scissors: ")

        if player1 == player1.upper() or player2 == player2.upper():
            print("Please enter lowercase letters only.")
            continue
        
        if player1 == player2:
            print("It's a tie!")
        elif player1 == 'rock' and player2 == 'paper':
            print("Player 2 wins!")
            player2_wins += 1
        elif player2 == 'rock' and player1 == 'paper':
            print("Player 1 wins!")
            player1_wins += 1
        elif player1 == 'paper' and player2 == 'scissors':
            print("Player 2 wins!")
            player2_wins += 1
        elif player2 == 'paper' and player1 == 'scissors':
            print("Player 1 wins!")
            player1_wins += 1
        elif player1 == 'rock' and player2 == 'scissors':
            print("Player 1 wins!")
            player1_wins += 1
        elif player2 == 'rock' and player1 == 'scissors':
            print("Player 2 wins!")
            player2_wins += 1
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
        
        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    
    print("Total rounds played:", rounds)
    print("Player 1 wins:", player1_wins)
    print("Player 2 wins:", player2_wins)

play()
