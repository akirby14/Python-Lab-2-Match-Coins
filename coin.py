'''
Matching Coins Program
Author: Adryiana Kirby
Purpose: The purpose of this program is to match coins or don't match coins. If player 1 matches player 2, player 1 wins and player 2 loses coins. If player 2 doesn't match player 1, player 2 wins and player 1 loses coins.
Date: 9/24/26
'''

import random

class Coin:
    def __init__(self):
        self.__sideup = random.choice(["Heads", "Tails"])

    def toss(self):

        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup