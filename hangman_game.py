
def play():

    print("********************************")
    print("  WELCOME TO THE HANGMAN GAME! ")
    print("********************************")

    secret_word = "banana"

    hanged = False
    hit = False

    while(not hanged and not hit):

        move = input("type a letter: ")
        move = move.strip()

        index = 0
        for letter in secret_word:
            if move.upper() == letter.upper():
                print("I found the letter {} in position {} ".format(move, index))
            index = index + 1

        print("Jogando..")



    print("End of the game!")

if(__name__ == "__main__"):
    play()