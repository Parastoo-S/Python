
''' Project Description
Author: Parastoo Saharkhiz


Project Name: Text Analysis, Character count

There is a menu with 5 options:

     option 1 opens and process all three files - Three stories , LesMiserables, TaleOfTwoCities, WarAndPeace 
     option 2- opens and process  LesMiserables
     option 3- opens and processTaleOfTwoCities
     option 4- opens and processWarAndPeace 
     option 5- opens and processSampleFile.txt, You can analyze your text: Open <SampleFile.txt> in <Input Files> directory, replace the text with yours and save it.
    
        In the last option (No 5), you can process your text by opening the file and replace it with you text and save it

Note:
Data files are saved in a sub directory in the pace where the program is running as <Input Files> 
Report files are saved in a sub directory in the pace where the program is running as <Output Result> 


'''

import os
import time

start_time=0 # this variable records the time of starting of the program
elapsed_time=0 # this variable hold the elapse time of processing of opening the file, generate report and save the file

fileName="" # this variable hold the name of the file to process
subDirInput="Input Files/"     # This directory is a sub directory in the place of the running program holds the text file to process 
subDirResult="Output Result/" # This directory is a sub directory in the place of the running program holds output result
report=""  # this variable holds the generated report to save in the file with the same file name with Report- prefix 

def main():  # This is the main progrm 
    
    global subDirInput
    global subDirResult
    global fileName  # this variable holds the name of the file 
    global elapsed_time
    global start_time  
    global report
    menu()  # this function shows the menu of the program
    a=getUserInput()   # getUserInput() gets the user selection
    start_time = time.time()
    if a==1: # this section process all three stories 
        report=""
        
        fileName="LesMiserables.txt"
        GenerateReport(subDirInput,fileName) # this sub routine process the file and generate the report
        
        fileName="TaleOfTwoCities.txt"
        GenerateReport(subDirInput,fileName)
        
        fileName="WarAndPeace.txt"
        GenerateReport(subDirInput,fileName)
        fileName= "Report-LesMiserables + TaleOfTwoCities + WarAndPeace.txt"
    if a==2: # this section process <LesMiserables.txt> file
        report=""
        subDirInput="Input Files/"
        
        fileName="LesMiserables.txt"
        GenerateReport(subDirInput,fileName)
    if a==3: # this section process <TaleOfTwoCities.txt> file
        report=""
        subDirInput="Input Files/"
        
        fileName="TaleOfTwoCities.txt"
        GenerateReport(subDirInput,fileName)
    if a==4: # this section process <WarAndPeace.txt> file
        report=""
        subDirInput="Input Files/"

        fileName="WarAndPeace.txt"
        GenerateReport(subDirInput,fileName)

    if a==5: # this section process <SampleFile.txt> file
        report=""
        subDirInput="Input Files/"

        fileName="SampleFile.txt"
        GenerateReport(subDirInput,fileName)
    
    print(report)
    SaveReport(report) # this sub routine save the generated report   
        
    elapsed_time = time.time() - start_time
    print("\nProgram completed in ",round(elapsed_time,8), " seconds")        

def GenerateReport(ubDirInput,fName): # this sub routine process the file and generate the report
    global fileName
    global subDirInput
    global report
    
    try:  # this section manage the error in opening of the file
    
        with open(subDirInput + fName, 'r', encoding="utf-8-sig") as file:
            contents = file.read()
        file.close()
        
        NumberOfSpace=contents.count(' ')
        NumberOfCharacters=len(contents)
        report+="\n"
        report+="\tFile Name : " + fileName + "\n" 
        report+="\tNumber of space characters : " + str(format (NumberOfSpace, ',d')) + "\n" 
        report+="\tTotal number of characters : " + str(format(NumberOfCharacters, ',d')) + "\n" 
        report+="\tPercentage of space in file : " + str(round((NumberOfSpace*100/NumberOfCharacters),2)) + " %" + "\n" 
    except IOError:
#         print ("Error: can\'t find file or read data")
        report="Error: can\'t find file or read data"

 
def SaveReport(report): # this sub routine saves the report in a text file with the same name as the open file with <Report-> prefix 
    global fileName
    global subDirResult
    try: # this section manage the error in writing the report in file 
        with open(subDirResult + "Report-" + fileName, 'w') as output_file:
            output_file.write(report)
        
        output_file.close()  
        
    except IOError:
        print ("Error: can\'t write data")
        

    
def menu(): # his is the main menu
    print("\nEnter a number as your selection:")
    print("\t 1- Three stories , LesMiserables, TaleOfTwoCities, WarAndPeace ")
    print("\t 2- LesMiserables")
    print("\t 3- TaleOfTwoCities")
    print("\t 4- WarAndPeace ")
    print("\t 5- SampleFile.txt, You can analyze your text: Open <SampleFile.txt> in <Input Files> directory, replace the text with yours and save it." )
    print("\t")

    
def getUserInput(): # this function gets the user selection
    while True: # it will stay in the loop until user enter a number between 1 to 5
        try: # this section checks the user just enter an integer number
             x = int(input("\nPlease enter a number as your selection: "))
             if x<6:
#                 break
                return x
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

main()
