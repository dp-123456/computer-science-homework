import random

Scores= []

def Guessing():
    Number= random.randint(1,100)
    Guess= 0
    Attempts= 0

    while Guess!= Number:
        try:
            Guess= int(input("Guess a number (1-100): "))
            if Guess< 1 or Guess> 100:
                        raise ValueError
            Attempts= Attempts+1

            if Guess>Number:
                print("too high!")
            elif Guess<Number:
                print("too low!")
            else:
                print("U guessed it right!")
                print("U got it in", Attempts, "Attempts!")

                Name= input("What is ur name? ")
                Scores.append([Name,Attempts])
        except ValueError:
            print("Pls enter a  number between 1 and 100!!")

while True:
     Guessing()
     Again= input("Play again? (y/n): ")
     if Again=="n":
          break
     print("-----------")
     print("LEADERBOARD")
     print("-----------")
     for Score in Scores:
          print(Score[0],"-", Score[1], "attempts")
