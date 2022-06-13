import random

def play():
    
    # wordrps=['Rock','Paper','Scissors']
    # rps=wordrps[]

    rps=['R','P','S']
    computer =random.choice(rps)
    user= input(""" Pick a weapon: 

                R for Rock
                P for Paper
                S for Scissors
                Enter Here: """)
    player=user.capitalize()
    
    while player not in rps: 
        player= input("""INVALID INPUT! Try Again.
                Pick a weapon: 
                    R for Rock
                    P for Paper
                    S for Scissors
                        Enter Here: """).capitalize()

    if player==computer:
        print("Player:", player ,"and CPU:",computer)
        print("It\'s a tie")
        return play()

    elif player =='P':
        if computer == "R":
            print("Player:(", player ,")and CPU:(",computer,")")
            print("You Win!!")
        if computer == "S":
            print("Player:", player ,"and CPU:",computer)
            print("You Lose!!")
          
    elif player == 'R':
        if computer == "P":
            print("Player:", player ,"and CPU:",computer)
            print("You Lose!!")
        if computer == "S":
            print("Player:", player ,"and CPU:",computer)
            print("You Win!!")

    elif player == 'S':
        if computer == "P":
            print("Player:", player ,"and CPU:",computer)
            print("You Win!!")
        if computer == "R":
            print("Player:", player ,"and CPU:",computer)
            print("You Lose!!")
            
play()





