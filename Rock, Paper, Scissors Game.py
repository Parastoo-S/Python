
'''
Author: Parastoo Saharkhiz

Game: Rock, Scissors, paper
- User can play several rounds without running the program again.
The result or all played rounds will be shown at the end of each round.

'''

import random

ListResult={}
ListResult[0,0]=0
ListResult[0,1]=0
ListResult[0,2]=0

index=0 # This variable shows the number of rounds played
YouWon=0 # This variable keeps the records of the number of times that user wins
ComputerWon=0 # This variable keeps the records of the number of times that computer wins
tie=0 # This variable keeps the records of the number of times that result i tie

tt = True
ttt= True
TopMark=10

def PlayRSP(): # this sub-routine is the main program
    global tt,ttt
    global tie, YouWon, ComputerWon, TopMark
    global index
    global ListResult
    print("Let's play or Rock, Paper, or Scissors! game")

    while ttt==True:    # This will control if the user want to finish the game and quit 
        while tt==True: # This while control the running the game, user can quit early in the game:
            ShowMenu()  
            u = GetUserInput()
            print("You have selected:",selection(u))
            c=GenerateComputerSelection()
            print("Computer selected:",selection(c))
            result=CheckWhoIsWiinner(u,c)
            KeepTrackofResults(result)
            print("\nResult By Now : Tie= ",tie, ", You Won=", YouWon, ",Computer Won:", ComputerWon)
            
            print("")
            if (YouWon==TopMark) or (ComputerWon==TopMark):
                FinalResult2() 
                tt= False
        ss="Do you want to play again (Y/N)?"
        Answer= UserResponse(ss)
        if Answer=='N':
            ttt=False
        else:
            print("Yes")
            index=index+1
            tie=0
            YouWon=0 
            ComputerWon=0
            tt=True
    print("\n Good Bye.")
   
    



def UserResponse(s):  # This sub-routine get the user response. it returns Y orN
    checkQuit=False
    while checkQuit == False:
        print("\n",s)
        userQ = input()
        if userQ == 'y' or userQ == 'Y' or userQ == 'n' or userQ == 'N':
            checkQuit = True
        else: 
            print("Invalid. Try Again. ")    
    if userQ == 'y' or userQ == 'Y':
        return('Y')
    else:
        return('N')
       
def ShowMenu(): # This sub-routine shows the menu and tell user what to do
    print("_____________________________________")
    print("\nEnter a number as your selection:")
    print(" \n 1) Rock \n 2) Paper \n 3) Scissors \n")
    
def GetUserInput(): # This sub-routine get the user selection in the game, selections provided in the menu
    check=1
    while check == 1:
        UserInput = input()
        if UserInput == '1' or UserInput == '2' or UserInput == '3':# or UserInput == '4':
            check = 2
        else: 
            print("Invalid. Try Again. ")
    return UserInput

def GenerateComputerSelection(): # This sub-routine random number between 1 to 3 as computer selection
    ComputerSelection=random.randint(1,3)
    computer=str(ComputerSelection)
    return computer

def selection(select): # This sub-routine converts the user selection (number) to text
    if select=='1':
        return 'Rock'
    if select=='2':
        return 'Paper'
    if select=='3':
        return 'Scissors'

def CheckWhoIsWiinner(userSelection,ComputerSelection): # This sub-routine determines who is winner in each round
    if userSelection == '1':
        if ComputerSelection == '1':
            print("Rock & Rock. You and computer both have selected Rock. Result is TIE.")
            return 0
        elif ComputerSelection == '2':
            print("Rock & Paper. Paper covers rock. So, the Computer is Winner.")
            return 2
        else:
            print("Rock & Scissors. Rock breaks scissors. So, you are Winner.")
            return 1
    elif userSelection == '2':
        if ComputerSelection == '1':
            print("Paper & Rock. Paper covers rock. So, you are Winner.")
            return 1
        elif ComputerSelection == '2':
            print("Paper & Paper.You and computer both have selected Paper. Result is TIE.")
            return 0
        else:
            print("Paper & Scissors. Scissors cut paper. So, the Computer is Winner.")
            return 2
    else: # player choice defaults to 3
        if ComputerSelection == '1':
#             print("31 Scissors & Rock. Rock breaks scissors. So, the Computer is Winner.")
            print("Scissors & Rock. Rock breaks scissors. So, the Computer is Winner.")
            return 2
        elif ComputerSelection == '2':
#             print("32 Scissors & Paper. Scissors cut paper. So, you are Winner.")
            print("Scissors & Paper. Scissors cut paper. So, you are Winner.")
            return 1
        else: # PC defaults to scissors
            print("Scissors & Scissor .You and computer both have selected Scissors. Result is TIE.")
            return 0

def KeepTrackofResults(r): # This sub-routine keeps the track of the result and save them in variable and List
    global tie, YouWon, ComputerWon
    global tie, YouWon, ComputerWon
    print("\nRound", index+1)
    if r==0: # Tie
        tie = tie + 1
        ListResult[index,0]=tie 
        return 0
    elif r==1:  #  You win
        YouWon = YouWon + 1
        ListResult[index,1]=YouWon
        return 0
    else:   #  Computer win
        ComputerWon = ComputerWon + 1
        ListResult[index,2]=ComputerWon
        return 0
    
def FinalResult2(): # This sub-routine prints the results of each round
    global ListResult
    global tie, YouWon, ComputerWon
    print("\n_____________________________________________________________________________________")
    print("\nThis is the Final result:")
#     print("Len: ",len(ListResult[0,0]))
    for i in range(index+1):
        print("Round:",i+1,"    Tie: ",ListResult[i,0]," times","    You Won:", ListResult[i,1]," times", "    Computer Won:",ListResult[i,2]," times") 

    print("_____________________________________________________________________________________\n")


    for i in range(index+1):
        if ListResult[i,1] > ListResult[i,2]:
            print("Round:",i+1," Winner is You") 
        else:
            print("Round:",i+1," Winner is Computer") 
        
    print("_____________________________________________________________________________________\n")



#     print("\n _________________________________________________________")

     
PlayRSP()
