import random
import os
import time
from threading import Timer
import getpass

 
def clear():
    os.system("clear")
 
# Set of instructions for Rock-Paper-Scissors
def rps_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()

def rps():
     
    global rps_matrix
    global game_map
    global name1,name2
 
    # Game Loop for each game of Rock-Paper-Scissors
    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
 
        print()
 
        

   
        # Player Input
        inp1 =  getpass.getpass("Enter your move : ")
        inp2 =  getpass.getpass("Enter your move : ")

        print(name1," choice is ", inp1)
        print(name2," choice is ", inp2)
        

        
        if inp1.lower() == "exit":
            clear()
            break  
        elif inp1 == '1':
            player1_move = 0
        elif inp1 == '2':
            player1_move = 1    
        elif inp1 == '3':
            player1_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()  
            continue
 
        
        if inp2.lower() == "exit":
            clear()
            break  
        elif inp2 == '1':
            player2_move = 0
        elif inp2 == '2':
            player2_move = 1    
        elif inp2 == '3':
            player2_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()  
            continue


        print()
        time.sleep(2)
        print(player1_move,player2_move)
        print(rps_matrix[player1_move][player2_move])
        winner = rps_matrix[player1_move][player2_move]
        print(winner)
        # Declare the winner 
        if winner == player1_move:
            print(name1, "WINS!!!")
        elif winner == player2_move:
            print(name2,"WINS!!!")
        else:
            print("TIE GAME")
 
        print()
        time.sleep(2)
        clear()
 
 # The main function
if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
    # Win-lose matrix for traditional game
    rps_matrix = [[-1, 1, 0],
                  [1, -1, 2],
                  [0, 2, -1]]
 
    name1 = input("Enter your name1: ")
    name2 = input("Enter your name2: ")
    
 
    # The GAME LOOP
    while True:
        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
            
        except ValueError:
            clear()
            print("Wrong Choice")   
            continue
 
        # Play the traditional version of the game
        if choice == 1:
            rps()
 
        # Quit the GAME LOOP    
        elif choice == 2:
            break
 
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")






timeout = 10
t = Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt = "You have %d seconds to choose the correct answer...\n" % timeout
answer = input(prompt)
t.cancel()