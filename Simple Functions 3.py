# Author: Parastoo Saharkhiz 
# Assignment 5

#######################
### 1a
#######################
def largest_34(a):
    '''(list)-> int

    the function largest_34 takes a list, a, as an input parameter and returns the
    sum of the 3rd and 4th largest values in the list

    '''

    b= sorted(a)
    return(b[-3]+ b[-4])


#######################
### 1b
#######################

def largest_third(a):
    '''(list)->int
    the function largest_third computes the sum of the len(a)//3 of the
    largest values in the list a
    '''
    
    x= len(a)//3
    b= sorted(a)
    l = b[-x:]
 
    list_sum=0
    for i in range (len(l)):
        list_sum=list_sum+ l[i]
        
    return(list_sum)


#######################
### 1c
#######################

def third_at_least(a):
    ''' (list)-> int/ str (int when the value is found, str if no matches were found 

    The function third_at_least that returns a value in a that occurs at
    least len(a)//3 + 1 times. If no such element exists in a, then this
    function returns None.

    '''
    b= sorted(a)

    index=1
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            index = index+1
            if index == (len(a)//3)+1:
                return b[i]
 
        else:
            index = 1
   
    return'None'



#######################
### 1d
#######################

def sum_tri(a,x):
    '''(list, int)-> bool
    The function sum_tri(a,x), takes a list , a, as input and returns True
    if there exists indices i, j and k such that a[i]+a[j]+a[k]=x.
    Otherwise it returns False.  
    '''
    
    for i in range (len(a)):
        
        for j in range (len(a)):
            
            for k in range (len(a)):

                if a[i]+a[j]+a[k] == x:

                    return True

    return False
