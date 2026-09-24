'''
Matching Coins Program
Author: Adryiana Kirby
Purpose: The purpose of this program is to match coins or don't match coins. If player 1 matches player 2, player 1 wins and player 2 loses coins. If player 2 doesn't match player 1, player 2 wins and player 1 loses coins.
Date: 9/24/26
'''

from coin import Coin

class Player:
    def __init__(self, name="Player 1"):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return Coin.get_sideup()

    def get_sideup(self):
        return self.__coin.get_sideup()

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name