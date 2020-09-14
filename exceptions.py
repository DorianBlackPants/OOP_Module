"""Module to control game process

"""

class GameOver(Exception):
    """Game control exception. Exception to end the game ( breakes a While loop ).

    """


class EnemyDown(Exception):
    """Game control exception. Creates a new enemy, raises a level.

    """


class Exit(Exception):
    """Game control exception. Breakes a While loop inside the attack/defence loop.

    """


class WrongInput(Exception):
    """Game control exception. Controls player input.

    """
