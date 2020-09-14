"""File for Player/Enemy classes.
Contains class "Score" for handling User Scores.

"""

from ast import literal_eval

from random import randint

from exceptions import GameOver, EnemyDown, Exit, WrongInput

from settings import NUMBER_OF_LIVES, WIN_CONDITIONS, Allowedmoves, MWR_LIST


class Enemy:
    """A class to represent an enemy.
    Attributes:
        level: variable(num)
        Lives: variable(num)
    Methods:
        select_attack: returns a random number from 1 to 3
        decrease_lives: decreases lives; raises exception when lives == 0
    """
    def __init__(self, level):
        """Constructs all the necessary attributes for the enemy object.

        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """returns a random number from 1 to 3

        """
        return randint(1, 3)

    def decrease_lives(self):
        """decreases lives; raises exception when lives  == 0 (False)

        """
        self.lives -= 1
        if self.lives:
            return self.lives
        raise EnemyDown


class Player:
    """A class to represent a player.
        Attributes:
            name: str
            score: variable(num)
            Lives: constant NUMBER_OF_LIVES
            allowed_attacks: constant (list)
        Methods:
            fight: returns round result
            decrease_lives: decreases lives; raises exception when lives == 0
            attack: returns attach result
            defence: returns defence result
            input_validar: validates user input
    """
    allowed_attacks = Allowedmoves.ALLOWED_ATTACKS.value

    def __init__(self, name):
        """Constructs all the necessary attributes for the player object.

        """
        self.name = name
        self.lives = NUMBER_OF_LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defence):
        """Returns round result
        Parameters:
                attack (int):  integer
                defence (int): integer

        Returns:
                int depending on win conditions

        """
        if attack == defence:
            return 0
        if (attack, defence) in WIN_CONDITIONS:
            return 1
        return -1

    def decrease_lives(self):
        """decreases lives; raises exception when lives  == 0 (False)

        """
        self.lives -= 1
        if self.lives:
            return self.lives
        raise GameOver

    def attack(self, enemy_obj):
        """Returns attack result
                Parameters:
                        self (str):  user input
                        enemy_obj (int): integer

                Returns:
                        int depending on fight() results

        """
        print("You are attacking!")
        user_input = self.input_validar((input("Enter your choice \n")))
        enemy_input = enemy_obj.select_attack()
        print(f"Enemy rolled: {enemy_input} ")
        if self.fight(user_input, enemy_input) == 0:
            print("It's a draw!")
        elif self.fight(user_input, enemy_input) == 1:
            self.score += 1
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        else:
            print("You missed!")

    def defence(self, enemy_obj):
        """Returns defence result
            Parameters:
                        self (str):  user input
                        enemy_obj (int): integer

                Returns:
                        int depending on fight() results

        """
        print("You are defending!")
        user_input = self.input_validar((input("Enter your choice \n")))
        enemy_input = enemy_obj.select_attack()
        if self.fight(enemy_input, user_input) == 0:
            print("It's a draw!")
        elif self.fight(enemy_input, user_input) == 1:
            print("Enemy smacked you in the face!")
            self.decrease_lives()
        else:
            print("Enemy missed!")

    def input_validar(self, user_input):
        """Validates user input
            Parameters:
                    user_input (str): input

            Returns:
                    variable (int)
            Raises:
                Exit (close program)
                WrongInput(Game control exception. Controls player input.)

        """
        if user_input in self.allowed_attacks:
            return MWR_LIST.get(user_input)
        if user_input in Allowedmoves.EXIT.value:
            raise Exit
        raise WrongInput


class Score:
    """A class for handling User Scores (Top 10).

        Methods:
            get_score: reads scores from file and converts to a dictionary
            by_value: function to help to sort a dict by values
            score_sorter: function to sort a dict by values
            make_high: appends new results
            show_score: shows leaderboard
            write_score: writes high-score to a file

    """
    @staticmethod
    def get_score():
        """Reads scores from file and converts to a dictionary
            Parameters:
                    text file (str): string

            Returns:
                    check_high_score (dict): converts to a dict using leteral_eval

        """
        with open("scores.txt", "r+") as check:
            check_high_score = literal_eval(check.read())
            return check_high_score

    @staticmethod
    def by_value(item):
        """Sorts a dict .items representation by values

        """
        return item[1]

    def score_sorter(self):
        """Sorts a dict .items representation by values,
        converts and limits only 10 entries
        Returns:
            (dict) : a dictionary sorted by values
             with not more than 10 key:value pairs

        """
        check_high_score = self.get_score()
        check_high_score = {k: v for k, v in sorted(check_high_score.items(), key=self.by_value, reverse=True)}
        check_high_score = dict(list(check_high_score.items())[0:10])
        return check_high_score

    def make_high(self, name, score):
        """Appends new results depending on User Name
            Parameters:
                    variable name (str): key for a dict
                    variable score (num): value for a dict
            Returns:
                    writes a new high-score to a file;
                    or updates a high-score for an existing user

        """
        new_data = {name: score}
        check_high_score = self.score_sorter()
        if name in check_high_score.keys():
            if score > check_high_score[name]:
                check_high_score.update(new_data)
                final = check_high_score
                final = {k: v for k, v in sorted(final.items(), key=self.by_value, reverse=True)}
                final = dict(list(final.items())[0:10])
                with open("scores.txt", "w+") as scwr:
                    scwr.write(str(final))
        else:
            new_data = f",\'{name}\': {score},"
            with open("scores.txt", "w+") as scwr:
                scwr.write(str(check_high_score)[0:-1] + " " + new_data +"}")
        final = self.score_sorter()
        with open("scores.txt", "w+") as scwr:
            scwr.write(str(final))

    @staticmethod
    def show_score():
        """Shows leaderboard
                Returns:
                    representation of high-score from a file
                    or raises exceptions if file is empty
                Raises:
                    SyntaxError, AttributeError (empty score file)

        """
        print("\t\t Leaderboard:")
        print("======================================")
        with open("scores.txt", "r+") as check:
            try:
                check_high_score = literal_eval(check.read())
                for key, value in check_high_score.items():
                    print(f"{key} == {value}")
            except SyntaxError:
                print("No HIGHSCORE yet")
            except AttributeError:
                print("No HIGHSCORE yet")

    def write_score(self, name, score):
        """Writes new results after a game
            Parameters:
                    variable name (str): key for a dict
                    variable score (num): value for a dict
            Returns:
                    updates or writes a new high-score to a file;


        """
        new_data = {name: score}
        try:
            self.make_high(name, score)
        except SyntaxError:
            with open("scores.txt", "w+") as scwr:
                scwr.write(str(new_data))
        except AttributeError:
            with open("scores.txt", "w+") as scwr:
                scwr.write(str(new_data))
