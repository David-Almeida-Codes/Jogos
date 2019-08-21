import random

def play():

    print("********************************")
    print("  WELCOME TO THE HANGMAN GAME! ")
    print("********************************")

    archive = open("words.txt", "r")
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    #print(words)

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