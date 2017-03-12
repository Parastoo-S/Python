#Name: Parastoo Saharkhiz 
# Student number:  8697886
# Course: ITI 1120B 
# Assignment Number 5 - Part 2

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

#######################################################################################

class Rectangle:
    '''class that represents a 2D (axis-parallel) rectangle'''


    def __init__(self, Point1,Point2, color):
        '''(Rectangle, Point, Point, str) -> None
            initialize Rectangle information to ((x,y),(x,y), color)'''
        
    
        self.bottom_left = Point1
        self.top_right = Point2 
        self.col = color
        self.pt1= self.bottom_left.get()
        self.pt2= self.top_right.get()

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other are the same rectangles'''

        return (self.bottom_left == other.bottom_left) and (self.top_right == other.top_right) and (self.col == other.col)


    def __repr__(self):
        '''(Rectangle)--> str
        Returns a string giving information regarding the Rectangle'''
        return ('Rectangle(Point'+str(self.pt1)+', Point'+str(self.pt2)+", '"+ self.get_color()+"')" )
 
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Rectangle(Point1, Point2, color).
        '''
               
        return 'I am a {} rectangle with bottom left corner at {} and top right corner at {}.'.format(self.get_color() ,self.pt1 , self.pt2)


    def get_bottom_left(self):
        '''(Rectangle)-> Point

        Returns the coordinates of the bottom-left corner of the rectangle
        '''    
        return self.bottom_left


    def get_top_right(self):
        '''(Rectangle)-> Point

        Returns the coordinates of the top-right corner of the rectangle
        '''

        return self.top_right

    def get_color(self):
        '''(Rectangle)-> str
        returns a string containing the color of the rectangle
        '''

        return str(self.col)


    def reset_color(self,col2):
        '''(Rectangle, str)-> None
        resets the color of the rectangle
        '''
        
        self.col= col2 
        
    def get_perimeter(self):
        '''(Rectangle)-> int
        calculates and returns the perimeter of the rectangle
        '''

        return 2*(self.top_right.x - self.bottom_left.x)+ 2*(self.top_right.y - self.bottom_left.y)


    def get_area(self):
        '''(Rectangle)-> int
        Calculates and returns the area of rectangle
        '''
        
        return (self.top_right.x - self.bottom_left.x)*(self.top_right.y - self.bottom_left.y)


    def move(self, dx, dy):
        '''(Rectangle, int, int) -> None
        moves the calling rectangle by dx in the x direction and by dy in the y-direction.
        '''
        
        self.bottom_left.move(dx,dy)
        self.top_right.move(dx,dy)
        self.pt1 = self.bottom_left.get()
        self.pt2 = self.top_right.get()
     


    def intersects(self,Rectangle):
        '''(Rectasngle, Rectangle)-> bool
        returns True if the calling rectangle intersects the given rectangle and False otherwise.
        '''
        
        return (((self.bottom_left.x)<=(Rectangle.top_right.x)<=(self.top_right.x))  or ((self.bottom_left.y)<=(Rectangle.top_right.y)<=(self.top_right.y))) and (((self.bottom_left.x)<=(Rectangle.bottom_left.x) <=(self.top_right.x)) or ((self.bottom_left.y) <= (Rectangle.bottom_left.y) <= (self.top_right.y)))



    def contains(self, x, y):
        '''(Rectangle, number, number)-> bool
        Returns True if the given a and y coordinate of a point is inside of the calling rectangle and False otherwise
        '''


        return ((self.top_right).x >= x >= (self.bottom_left).x) and ((self.top_right).y >= x >= (self.bottom_left).y)


    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other are the same rectangles'''

        return (self.bottom_left == other.bottom_left) and (self.top_right == other.top_right) and (self.col == other.col)


    def __repr__(self):
        '''(Rectangle)--> str
        Returns a string giving information regarding the Rectangle'''
        return ('Rectangle(Point'+str(self.pt1)+', Point'+str(self.pt2)+", '"+ self.get_color()+"')" )
 
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Rectangle(Point1, Point2, color).
        '''
               
        return 'I am a {} rectangle with bottom left corner at {} and top right corner at {}.'.format(self.get_color() ,self.pt1 , self.pt2)


#######################################################################################

class Canvas:

    def __init__(self):
            '''(Canvas)-->None
            Makes a Canvas as a blank list'''
            self.canvas= []

    def __repr__(self):
        '''(Canvas)--> str
        Returns information about the canvas'''

        return "Canvas (" + str(self.canvas)+")"    



    def add_one_rectangle(self, rectangle):
        '''(Canvas, Rectangle)--> list
        Appends the rectangle to the given list'''

        
        return (self.canvas).append(rectangle)

        
    def count_same_color(self,thecolor):
        '''(Canvas, str)--> int
        Returns the number of apperances of a color in the Canvas list'''
        
        self.colors=[]
        for color in self.canvas:
            (self.colors).append(color.get_color())
        return self.colors.count(thecolor)


    def __len__(self):
        '''(Canvas)-> list
        returns length of the list self.canvas
        '''
        
        return len(self.canvas)
        
        
        
    def total_perimeter(self):
        '''(Canvas)-> int
        Calculates and returns the sum of the perimeters of all the rectangles in the calling canvas.
        '''
        
        tot_p = 0
        for i in range(len(self)):
            tot_p = tot_p +((self.canvas[i]).get_perimeter())
        return tot_p



    def min_enclosing_rectangle(self):
        '''(Canvas)-> Point, Point, str
        Calculates the minimum enclosing rectangle that contains  all the rectangles in the calling canvas
        and returns an object of type Rectangle 
        '''

        self.x_min=(self.canvas[0]).bottom_left.x
        self.x_max=(self.canvas[0]).top_right.x
        self.y_min=(self.canvas[0]).bottom_left.y
        self.y_max=(self.canvas[0]).top_right.y

        for corner in self.canvas:
            
            if corner.bottom_left.x<self.x_min:
                self.x_min = corner.bottom_left.x
                
            if corner.top_right.x>self.x_max:
                self.x_max = corner.top_right.x
                
            if corner.bottom_left.y<self.y_min:
                self.y_min = corner.bottom_left.y
                
            if corner.top_right.y>self.y_max:
                self.y_max = corner.top_right.y
                
        return (Rectangle(Point(self.x_min,self.y_min),Point(self.x_max,self.y_max),'green'))



    def common_point(self):
        '''(Canvas)-> bool/str (str if not enought rectangles were given to compare)

        Returns True if there exists a point  that intersects all rectangles in the calling canvas. False otherwise.
        
        '''


        if len(self.canvas)>1:
            x= self.canvas[:]
            for i in self.canvas:
                x.remove(i)

                for j in x:
                    if not (j.intersects(i)):
                        return True

            return False

        else:
            return "Not enought rectangles to compare."


