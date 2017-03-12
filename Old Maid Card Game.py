#Author: Parastoo Saharkhiz 
# Old Maid Card Game

import random
dealer=[]


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=deck[:25]
     human=deck[25:]

     return (dealer, human)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    l.sort()
    c=0

    while len(l)-1>c:
        if (l[c][0]==l[c+1][0]): #if the number on the cards are the same, remove both
            l.remove(l[c+1])
            l.remove(l[c])
            c=c-1
        c=c+1
    no_pairs=l


    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''


    print(*deck)
    print("\n")
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''


     print("I have",n," cards. If 1 stands for my first card and",n,"\nfor my last card, which of my cards would you like?")
     while True:

        print("Please enter integer between 1 and",n,":")
        m=int(input())

        if (1<= m) and (m<= n):
            break
        print('invalid number')

     print("You asked for my ",m,ordinal_indicator(m)," card")
     
     return(m)


def show_human_deck(human):
    print("**********************************************")
    print("Your turn\n")
    print("Your current deck is: \n")
    print_deck(human)
    
def ordinal_indicator(x): #indicates the suffix for the input number
    if x==1:
        return "st"
    elif x==2:
        return "nd"
    elif x==3:
        return "rd"
    else:
        return "th"
    
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)#unpacks the list of Human deck, displays it
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()

     dealer=remove_pairs(dealer)#removes pairs and shuffles dealer's deck
     human=remove_pairs(human) #removes pairs and shuffles human's deck


     
     while ((len(dealer)>1) or (len(human)>1)): #Run until one of them runs out of card
        show_human_deck(human)

        input_h=get_valid_input(len(dealer))

        print("Here it is. it is ",dealer[input_h-1],"\n") #finds the card at the position human picked
        print("With",dealer[input_h-1]," added, your current deck of card is:\n")
        human.append(dealer[input_h-1])#adds the card (from dealer's deck) to human's deck
        print(*human)
        print("\nAnd after discarding and shuffling, your deck is:\n")
        dealer.remove(dealer[input_h-1]) #removes that card from dealer's deck
        remove_pairs(human)#remove duplicates from human
        print(*human)
        print("\n")

        
        if len(dealer)==0: #if after human picked from dealer, dealer runs out of card, stop the game
            break
        
        wait_for_player()
        print("**********************************************")
        print("My Turn")
        
        x=random.randint(1,len(human)) #dealer picks randomly from human

        print("I picked your ",x,ordinal_indicator(x)," card")
        

        dealer.append(human[x-1])#adds the card (from human's deck) to dealer's deck
        human.remove(human[x-1])#removes that card from human's deck
        remove_pairs(dealer)#remove duplicates from dealer

        print("\n")
        if len(human)==0: #if after dealer picked from human, human runs out of card, stop the game
            break
        wait_for_player()
        
     if len(dealer)==0: #when out of loop, if Human has the Queen
            print("Ups, I do not have any more cards\nYou lost! I, Robot, win")
     else: #if dealer has the Queen 
            print("Ups, you do not have any more cards\nCongratulations, You, Human, win")
	 

# main
play_game()
