"""Settings file. Contains all constants.

"""

from enum import Enum

class Allowedmoves(Enum):
    """Class to store allowed attacks and exit, for attacck/defend loop.

    """
    ALLOWED_ATTACKS = ("1", "2", "3")
    EXIT = "exit"


NUMBER_OF_LIVES = 10
MAGE = 1
WARRIOR = 2
ROGUE = 3
MWR_LIST = {'1': MAGE,
              '2': WARRIOR,
              '3': ROGUE
              }

WIN_CONDITIONS = [(MAGE, WARRIOR), (WARRIOR, ROGUE), (ROGUE, MAGE)]
'''Mage beats Warrior, Warrior beats Rogue, Rogue beats Mage'''

def show_instructions():
    """Function to show available commands in game menu.

    """
    print("--------------------------------------")
    print("Enter \"start\" to play;")
    print("Enter \"exit\" to quit;")
    print("Enter \"help\" to show instructions;")
    print("Enter \"hs\" to show scores.")
    print("--------------------------------------")
    print("\t\tEpic Clash rule set:")
    print("--------------------------------------")
    print("Mage beats Warrior, Warrior beats Rogue, Rogue beats Mage")
    print("--------------------------------------")
    print("\t\tInGame controls:")
    print("--------------------------------------")
    print("Enter 1 - for Mage, 2 - for Warrior, 3 - for Rogue")
    print("Enter \"exit\" to quit.")
    print("--------------------------------------")
