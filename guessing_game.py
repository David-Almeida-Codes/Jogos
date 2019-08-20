import random

def play():

    print("********************************")
    print("  WELCOME TO THE GUESSING GAME! ")
    print("********************************")

    secret_number = random.randrange(1,101)
    attempts = 0
    game_round = 1
    points = 1000

    print("----- difficulty levels! -----")
    print("(1) Easy (2)Medium (3)difficult")

    level = int(input("Enter your level: "))

    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    else:
        attempts = 5    

    for game_round in range(1, attempts + 1):
        #print("Number: ", secret_number)
        print("Attempt {} of {} ".format(game_round, attempts))
        move = int(input("Type your number move: "))
        print("You typed: ", move)

        if(move < 1 or move > 100):
            print("you must enter a number in 1 and 100")
            continue

        won = move == secret_number
        bigger = move > secret_number
        smaller = move < secret_number

        if won:
            print("YOU WON! AND MADE {} POINTS".format(points))
            break
        else:
            if bigger:
                print("YOU LOSE, YOUR NUMBER IS BIGGER THAN THE SECRET NUMBER")  
            elif smaller:
                print("YOU LOSE, YOUR NUMBER IS SMALLER THAN THE SECRET NUMBER") 
            
            lost_points = abs(secret_number - move)
            points = points - lost_points

    print("end of the game")


if(__name__ == "__main__"):
    play()