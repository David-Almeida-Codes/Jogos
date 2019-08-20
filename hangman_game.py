
def play():

    print("********************************")
    print("  WELCOME TO THE HANGMAN GAME! ")
    print("********************************")

    secret_word = "banana"
    hit_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    hit = False

    print(hit_letters)


    while(not hanged and not hit):

        move = input("type a letter: ")
        move = move.strip()

        index = 0
        for letter in secret_word:
            if move.upper() == letter.upper():
                hit_letters[index] = letter
            index = index + 1

        print(hit_letters)



    print("End of the game!")

if(__name__ == "__main__"):
    play()