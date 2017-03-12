#Name: Parastoo Saharkhiz 
# Assignment 5

def digit_sum(n):
    '''(int)-> int
    The recursive function digit_sum takes an integer as an input and
    calculates the sum of all digits of the given integer n.
    '''

    if n == 0:
        return 0

    else:
        return (n%10) + digit_sum(n//10)
        


def digital_root(n):
    '''(int)-> int
    The recursive function digital_root takes n as an input and first calulates
    sum of all of the digits in a number, and repeating the process
    with the resulting sum until only a single digit remains.
    '''
   

    if n<10:
        return n

    
    return digital_root(digit_sum(n))
