#Author: Parastoo Saharkhiz 
# Assignment 2


###################################################################
# Question 1
###################################################################

def size_format(b):
    '''(integer)-> string
    Function size_format takes numbers of bytes (b), and returns a
    string with the b converted to bite/kilobyte/megabyte/gigabyte/terabyte
    '''

    if(b>=0 and b<1000):
        return str(b)+"B"

    elif(b>=1000 and b<1000000):
        x= round((b/1000),1)
        return str(x)+"KB"

    elif(b>=1000000 and b<1000000000):
        y= round((b/1000000),1)
        return str(y)+"MB"
    elif (b>=1000000000 and b<1000000000000):
        z= round ((b/1000000000),1)
        return str(z)+"GB"
    elif(b>=1000000000000):
        w= round ((b/1000000000000),1)
        return str(w)+"TB"
    else:
        return "buy a new hard disk"
        
    
###################################################################
# Question 2
###################################################################

def add_article(s):
    '''(string)->string
    Function add_article takes as input a string s containing a name of a country
    and returns a string with article added: le for masculine and la for feminine,
    l’ for country names that start with a vowel, les for Etats-Unis and les Pay-Bas.
    '''
    if s=='Etats-Unis' or s=='Pay-Bas':
        print("les",s)
        
    elif s[0]=='A' or s[0]=='E' or s[0]=='I' or s[0]=='O' or s[0]=='U':
        print("l'",s)

    elif s=='Belize' or s=='Cambodge' or s=='Mexique' or s=='Mozambique' or s=='Zaire' or s=='Zimbabwe':
        print("le",s)
        

    elif s[-1]=='e':
        print ("la",s)

        
    else:
        print("le",s)


###################################################################
# Question 3
###################################################################

def factorial(n):
    '''integer-->number
    Function factorial takes a number and returns the factorial of the number
    '''

    if n == 0:
        return(1)
    
    else:
        return(n * factorial(n-1))


###################################################################
# Question 4
###################################################################

def special_count(l):
    '''(list)->number
    Function special_count takes as input a none-empty list of integers (l) and retruns the number of
    special integers it contains. A integer is special if non-negative and divisible
    by four, except that any non-negative integer divisible by 100 is not special
    unless it is also divisible by 400.
    '''

    counter = 0
    for i in l:
        if (i>=0) and (i % 4==0) and (i%100!= 0):
            counter = counter + 1
        elif 0 <= i and i % 400 == 0:
            counter = counter + 1
    return counter


###################################################################
# Question 5
###################################################################

def vote():
    '''none-->none
    Function vote takes users input, and returns whether or not the vote will pass
    depedning on how many of each type of vote was casted.
    '''
    x=input("Enter the yes, no, abstained votes one by one and then press enter: \n")
    v=x.replace(',',' ')
    v=v.split()

    y=0
    n=0
    for i in v:
        a=i.lower()
        if a=='yes' or a=='y':
            y=y+1
        elif a=='no' or a=='n':
            n=n+1

    total=y+n

    if y==total:
        print("Proposal passes unanimously.")

    elif y/total>=(2/3):
        print("Proposal passes with super majority.")
           
    elif y/total<(2/3) and y/total>=(1/2):
        print("Proposal passes with simple majority.")

    else:
        print("Proposal fails.")




###################################################################
# Question 6
###################################################################
import random

x=[]

def stats_v1(n):
    '''(integer)->(number)
    function stats_v1 and stats_v2 take as input a positive integer (n), produce n random integers in the
    range [-100, 100], and print all those integers, the minimum of all those
    integers and the average of all those integers.
    '''

    for i in range(n):
        randint=random.randint(-100,100)
        x.append(randint)

    average=0
    for i in x:
        average=average+i
        average= average/n

    print("The minimum and the average of the following numbers:\n",x,"\nis",min(x),"and", average)



def stats_v2(n):
    integer=0
    value=500
    print("The minimum and the average of the following numbers:")
    for i in range (n):
        randint=random.randint(-100,100)
        print(randint, end=' ')
        if randint<value:
            value = randint

        integer=integer+randint
    integer=integer/n
    print("\nis",value,"and",integer)

    
###################################################################
# Question 7
###################################################################

def emphasize(s):
    '''(string)->string
    Function emphasize takes as an input a string s and retruns a string with a blank
    space inserted between every pair of consecutive letters in s.
    '''

    string=''
    for i in s:
        i=i+' '
        string= string+i
    return string


###################################################################
# Question 8
###################################################################


def crypto(s):
    '''(string)->string
    Function crypto takes as an input a string s and retruns encrypted string.
    The encryption proceeds as follow:last, first, second_to_last, second,
    third_from_the_back, third... .'''
    x=1
    y=' '
    for i in range(len(s)):
        if x==1:
            y=y+s[-1]
            s= s[0:-1]
            x=x*-1

        else:
            y=y+s[0]
            s=s[1:]
            x=x*-1

    return y

###################################################################
# Question 9
###################################################################

def stranger_things(l1,l2):
    '''(list)->bool
    Function stranger_things takes as an input two non-empty lists.
    The elements of that list can be numbers, strings or boolean values.
    the function returns true or false under cetain conditions'''

    counter=0
    for a in range(0, len(l1)):
        if a%2==0 and l1[a] == l2[a]:
            counter=counter+1
                   
    for b in range(0, len(l1)):
        if b%2!=0 and l1[b]!=l2[a]:
                counter=counter+1

    m=len(l1)
    n=len(l2)
    if m==counter and n==counter:
        return True
    else:
        return False


