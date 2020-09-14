"""Main Game Module.

"""

from exceptions import GameOver, EnemyDown, Exit, WrongInput

from models import Enemy, Player, Score

from settings import show_instructions

def play():
    """Main Game function.

    """
    player_name = input("Enter your name: ")
    print("\t\tEpic Clash rule set:")
    print("--------------------------------------")
    print("Mage beats Warrior, Warrior beats Rogue, Rogue beats Mage")
    print("Enter \"1 - for Mage\",\" 2 - for Warrior\",\"3 - for Rogue\"")
    print("--------------------------------------")
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)
    scoring = Score()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
            print("Round is over")
            print(f"Enemy HP: {enemy.lives}")
            print(f"Player HP: {player.lives}")
            print(f"Player Score: {player.score} points")
            print("--------------------------------------")
        except WrongInput:
            print("Wrong Input!!")
        except EnemyDown:
            print("Enemy down!")
            level += 1
            enemy = Enemy(level)
            player.score += 5
            print(f"Player Score: {player.score} points")
            print()
            print("New abomination rises!")
            print("--------------------------------------")
        except GameOver as message:
            print()
            print(f"Player Score: {player.score} points")
            scoring.write_score(player_name, player.score)
            raise GameOver from message


if __name__ == '__main__':
    print()
    print("\t\tWelcome to Epic Clash!")
    print()
    show_instructions()
    final_score = Score()
    while True:
        inp = input("Enter your choice = ")
        if inp.lower() == "help":
            show_instructions()
            continue
        if inp.lower() == "hs":
            final_score.show_score()
            print("======================================")
            continue
        if inp.lower() == "exit":
            break
        if inp.lower() == "start":
            try:
                play()
            except GameOver:
                print("Game over!")
                break
            except KeyboardInterrupt:
                pass
            except Exit:
                break
            finally:
                print("Good bye!")
        else:
            print("Wrong Input!!")
            continue
