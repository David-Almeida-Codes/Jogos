
def play():

    print("********************************")
    print("  WELCOME TO THE HANGMAN GAME! ")
    print("********************************")

    secret_word = "maca".upper()
    hit_letters = ["_" for letter in secret_word]

    hanged = False
    hit = False
    error = 0

    print(hit_letters)


    while(not hanged and not hit):

        move = input("type a letter: ")
        move = move.strip().upper()

        if move in secret_word:
            index = 0
            for letter in secret_word:
                if move == letter:
                    hit_letters[index] = letter
                index += 1
        else:
            error +=  1

        hanged = error == 6
        hit = "_" not in hit_letters
        print(hit_letters)

    if hit:
        print("YOU WON! :)")
    else: 
        print("YOU LOSE! :(")    

    print("End of the game!")

if(__name__ == "__main__"):
    play()