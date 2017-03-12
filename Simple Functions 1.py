#Author: Parastoo Saharkhiz
#Assignment #1

##Call Each function in the shell seperately

import turtle
import math 

########################################################
# Question 1
########################################################

def lbs2kg(w): #Converts pounds(lb) to kg
    '''(number)->number'''
       
    return (w*0.45359237)



########################################################
# Question 2
########################################################
def id_formater(fn, ln, appelation, city, year):
    '''name,name,name,name,int-> str,str,name,name,int'''
    x=appelation+'. '+ ln+', '+ fn+' ('+ city+', '+str(year)+')'
    return  x




########################################################
# Question 3
########################################################
def limerick_maker(): #creates a personalized limerick based on your name and city
    name=input("Enter your name: ")
    city=input("Enter your city of birth: ")
    
    print(str(name)+" had funny funny hair\nWith tons and tons to spare\n"+str(name)+"'s clippings made a wig\nIt was very big\nAnd caused the townsfolk of "+str(city)+" to stare")          




########################################################
# Question 4
########################################################
def id_formater_display(): 

    fn=input("What is your first name?: ")
    ln= input("What is your last name?: ")
    appelation=input("What is your appelation?: ")
    city=input("Where were you born?: ")
    year=input("What is your year of birth?: ")

    print(id_formater(fn, ln, appelation, city, year))


########################################################
# Question 5
########################################################
def l2loz(w):
    
    l=int(w)
    o=((w-int(w))*16)
              
    return l,o


########################################################
# Question 6
########################################################
def draw_soccer_field(): #Draws a soccor field using python turtle
    import turtle


    wn=turtle.Screen()
    t=turtle.Turtle()

    wn.bgcolor("green")
    t.pencolor("white")
    t.pensize(3)
    #1
    t.penup()
    t.goto(300,-200)
    t.pendown()
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.left(90)

    #2
    t.penup()
    t.goto(300,50)
    t.pendown()

    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(40)
    t.left(90)

    t.penup()
    t.goto(300,100)
    t.pendown()

    #3
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(90)
    t.right(90)

    t.penup()
    t.goto(-300,50)
    t.pendown()
    #4
    t.left(90)

    t.forward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)

    t.penup()
    t.goto(-300,100)
    t.pendown()


    #5
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(90)
    t.right(90)

    #6
    t.penup()
    t.goto(0,-200)
    t.pendown()

    t.forward(400)

    t.penup()
    t.goto(50,0)
    t.pendown()

    #7
    t.circle(50)

    #8
    t.penup()
    t.goto(-210,-40)
    t.pendown()
    t.right(90)

    t.circle(40,180)


    #9
    t.penup()
    t.goto(210,40)
    t.pendown()

    t.circle(40,180)

    #10
    t.penup()
    t.goto(-300,180)
    t.pendown()

    t.circle(20,90)


    #11
    t.penup()
    t.goto(-280,-200)
    t.pendown()

    t.circle(20,90)

    #12
    t.penup()
    t.goto(300,-180)
    t.pendown()

    t.circle(20,90)


    #13
    t.penup()
    t.goto(280,200)
    t.pendown()

    t.circle(20,90)

    #14
    t.penup()
    t.goto(0,0)
    t.pendown()

    t.dot(10,"white")

    #15
    t.penup()
    t.goto(240,0)
    t.pendown()

    t.dot(10,"white")

    #16
    t.penup()
    t.goto(-230,0)
    t.pendown()

    t.dot(10,"white")

    
 
########################################################
# Question 7
########################################################
def median3(num1,num2,num3): #Finds a median between 3 numbers
   '''(number,number,number)-> None'''
   
   x=((num1>=num2) and (num1<=num3)) or ((num1>=num3) and (num1<=num2))
   y=((num2>=num1) and (num2<=num3)) or ((num2>=num3) and (num2<=num1))
   z=((num3>=num1) and (num3<=num2)) or ((num3>=num2) and (num3<=num1))
   print(num1,"is a median. That is", x)
   print(num2,"is a median. That is",y)
   print(num3,"is a median. That is",z) 
   


########################################################
# Question 8
########################################################
def below_parabola(a,b,p,q): 
    '''int,number,number,number-> bool
    checks if a point in the plane
    x-coordinate p and y-coordinate q) is below or on the graph of the
    parabola y=ax^2 + b
    '''
   
    return 0>=(q-((a*(p**2))-b))


########################################################
# Question 9
########################################################
def projected_grade(a1,A1,a2,A2,m,M):

    Assignment1=a1/A1*0.05
    Assignment2=a2/A2*0.05
    Assignment3=((Assignment1+Assignment2)/2)
    Midterm=m/M*0.35
    Final=m/M*0.50
    grade=(Assignment1+Assignment2+Assignment3+Midterm+Final)
    return (grade*100)


########################################################
# Question 10
########################################################
def projected_grade_v2():

    a1= input("How many points did you get in Assignment 1? ")
    A1= input("What was the maximum possible number of points for Assignment 1? ")
    a2= input("How many points did you get in Assignment 2? ")
    A2= input("What was the maximum possible number of points for Assignment 2? ")
    m= input("How many points did you get on the midterm? ")
    M=input("What was the maximum possible number of points for the midterm?") 

    weighted_average=int(m)/int(M)*100
    Mark=projected_grade(int(a1),int(A1),int(a2),int(A2),int(m),int(M))
    
    if weighted_average<=50:
        print("Your predicted final grade is ",min(Mark,weighted_average),"%")

    else:
        print("Your predicted final grade is ",Mark,"%")



########################################################
# Question 11
########################################################
def change_to_coins(amount):
    x=round(amount*100)
    q=int(x)//25
    x=x%25
    d=x//10
    x=x%10
    n=x//5
    p=x%5
    
    
    return (q,d,n,p)





