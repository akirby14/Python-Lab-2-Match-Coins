'''
Matching Coins Program
Author: Adryiana Kirby
Purpose: The purpose of this program is to match coins or don't match coins. If player 1 matches player 2, player 1 wins and player 2 loses coins. If player 2 doesn't match player 1, player 2 wins and player 1 loses coins.
Date: 9/24/26
'''

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    choice = input("Do you want to toss the coin? (y/n): ")

    while choice.lower() == "y" and player1.get_wallet() > 0 and player2.get_wallet() > 0:

        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print(f"\nGame over, {player1.get_name()} or {player2.get_name()} has no more coins!")
            break

        player1.toss_coin()
        player2.toss_coin()

        print("\nTossing...")
        print(f"{player1.get_name()} tossed: {player1.get_sideup()}")
        print(f"{player2.get_name()} tossed: {player2.get_sideup()}")

        if player1.get_sideup() == player2.get_sideup():
            print(f"...It's a Match! {player1.get_name()} wins a coin!")
            player1.win_coin()
            player2.lose_coin()
        else:
            print(f"...No Match! {player2.get_name()} wins a coin!")
            player2.win_coin()
            player1.lose_coin()

        print(f"\n{player1.get_name()} has: {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has: {player2.get_wallet()} coins.")

        choice = input("\nDo you want to toss the coin? (y/n): ")

    if choice.lower() == "n":
        print("\n--- Final Score ---")
        print(f"{player1.get_name()}: {player1.get_wallet()}")
        print(f"{player2.get_name()}: {player2.get_wallet()}")
        
        if player1.get_wallet() > player2.get_wallet():
            print(f"{player1.get_name()} wins the game!")
        elif player2.get_wallet() > player1.get_wallet():
            print(f"{player2.get_name()} wins the game!")
        else:
            print("It's a Draw!")

print("\n--- Coin Match Game ---")
main()