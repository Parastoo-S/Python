# Developer: Parastoo Saharkhiz
  
def PlayGameGame():
    listResult=[] # This list holds the results of the calculations
    index=1 # This index control whether user wants to do another game or not
    validNumberCheck=1 # this variable used to check that the user Not to enter negative number  
#     iteration=0
    print("Hello. Let's begin the game")
    print("_________________________________________\n")
     
    while (index==1):
        while (validNumberCheck==1): # this while is to ensure that the user enter only a decimal number (no negative or decimal number)
            print("\nPlease enter an integer number bigger than 1 (No 0, No Negative, No Decimals): ",)
            b1=float(input())
            if b1<0: # to check if the user have entered negative number
                print("\nYou have entered a negative number.  Try Again.")
            elif b1==0: # to check if the user have entered 0
                print("\nYou have entered 0. Try Again.  ")
            elif b1==1:# to check if the user have entered 1
                print("\nYou have entered 1. Try Again.  ")
            elif (b1-int(b1))>0 : # to check if the user have entered a decimal number
                print("\nYou have entered a decimal number. Try Again. ")
            else:
                validNumberCheck=2 # validNumberCheckto changes  get out of while loop
        b = int(b1)
        OriginalNumber=int(b)

        while (b > 1): # This while is the main part of the program and execute the algorithm of the game 
            a=b % 2
            if a == 0:
                b=int(b/2)
            else:
                b=int(b*3+1)
            listResult.append(b) # Result is saved (append) in a list
        print("____________ Analysis Completed Successfully in  ", len(listResult), " iterations.________________________\n")

        UserSelection = input("Do you want to see the results and data in iterations (Y for yes, any other for No) ? ")
        if(UserSelection =="y" or UserSelection =="Y"): # check if the user wants to repeat the game
            print("_____________________________Results_________________")
            print("\nOriginal Number : ", OriginalNumber)
            for i in range(len(listResult)): 
                print(listResult[i])
            print("\nOriginal Number : ", OriginalNumber)
            print("____________ Analysis Completed Successfully in  ", len(listResult), " iterations.________________________\n")
        UserSelection = input("\nWould you like to play again (Y for Yes, any other key for No) ? ")
        if(UserSelection =="y" or UserSelection =="Y"): # check if the user wants to repeat the game
            print("\n")
            index=1 # reset index for new game
            del listResult[:] # clear the list to make it ready for new game 
            validNumberCheck=1 # reset validNumberCheck for new game
        else: 
            index=2 # chenge index to 2 to end  the game
    print("\nGood bye")   
# main
PlayGameGame() # the main program 
