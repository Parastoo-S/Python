# Developer: Parastoo Saharkhiz


# This program responds to the user action in selecting of one of the three buttons (type of language) 
# and say "Hello" in that selected language (English, Spanish and French)


from tkinter import *


class HelloApp:

    def __init__(self, master):  # Begin of the Constructor

        self.label = Label(master, text = "Hello")     # Initiation value of comment of the label
        self.label.grid(row = 0, column = 1, columnspan = 2)     # Positioning the label on row 0 and column 1
        
        # Defining the "English" button and positioning 
        Button(master, text = "English",        
                   command = self.English_hello).grid(row = 1, column = 0)

        # Defining the "Spanish" button and positioning 
        Button(master, text = "Spanish",
                   command = self.Spanish_hello).grid(row = 2, column = 2)

        # Defining the "Bonjour" button and positioning 
        Button(master, text = "Bonjour",
                   command = self.Bonjour_hello).grid(row = 3, column = 3)

    def English_hello(self):
        self.label.config(text = 'Hello')

    def Spanish_hello(self):
        self.label.config(text = 'Aloha')

    def Bonjour_hello(self):
        self.label.config(text = 'Bonjour')
            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
