import guessing_game
import hangman_game

def game():
    print("********************************")
    print("       CHOOSE YOUR GAME         ")
    print("********************************")

    print("(1) guessing game (2) hangman game")

    game = int(input("which game: "))

    if game == 1:
        print("playing guessing game")
        guessing_game.play()
    elif game == 2:
        print("playing hangman game")
        hangman_game.play()

if(__name__ == "__main__"):
    game()