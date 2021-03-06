#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import platform
import sys
import pickle 

#TODO Need the falttening to act as constants when instatiating this class multiple times

# This class holds all important system information and user data
class Program: 
    #Unflatten Class
    def load(self):
        f = open("flats/program.pickle","rb")
        tmp_dict = pickle.load(f)
        f.close()    
        self.__dict__.clear()      
        self.__dict__.update(tmp_dict) 

    #Flatten Class
    def save(self):
        f = open("flats/program.pickle","wb")
        pickle.dump(self.__dict__, f)
        f.close()

    def __init__(self): 
        # Check for New User / Previously Instantiated Class
        try:
            self.load()
        except: 
            self.newUser()
            self.save()

    def __del__(self):
        try: 
            #Set chaning Members to null before flattening
            del self.dateTime
        except:
            pass
        finally:
            self.save()

    # Pull Operating System ("Windows,"Linux","Darwin")
    def getOS(self):
        self.os = platform.system()
        return self.os

    # Pull Current DateTime (yyyyMMdd_hhmmssss)
    def getDateTime(self): 
        #TODO Have not decided best format yet
        print ("Date Time Under Construction")
        self.dateTime = "17760704_00000000"
        return self.dateTime

    # Prompts user to update directory information
    def getPrefDirectory(self):
        self.dir = input("Please enter your folder path: ") 
        while not (os.path.isdir(self.dir)):
            print("This folder was not found. Please Create and Try Again")
            self.dir = input("Please enter your folder path: ") 
        return self.dir

    def getPrefEditor(self):
        self.editor = "VS Code"
        #TODO Havent Decided best way to open the developmet environemnt
        print ("GetPrefEditor is Under Construction")
        return self.editor

    def getPrefLanguage(self):
        self.lang = input("Please enter your programming language: ") 
        while not(self.lang == "Python" or self.lang == "C/C++"):
            print("I'm sorry, we are currently only supporting 'Python' or 'C/C++.'")
            self.lang = input("Please enter your programming language: ") 
        return self.lang

    def getPrefName(self):
        self.author = input("Please enter your name/alias: ")
        return self.author

    def getProbCount(self):
        return self.probCount

    def newProblemID(self):
        self.probCount += 1
        return self.probCount

    def newUser(self):
        self.probCount = 0
        name = self.getPrefName()
        lang = self.getPrefLanguage()
        folder = self.getPrefDirectory()
        editor = self.getPrefEditor()

        print("Please review the following settings: Your name is " + name + ", who speaks in the toung of " + lang + ", in the land of " + folder + " and you use " + editor + " as your weapon of choice against evil!\n")
        confirmation = input("Press enter to continue or type 'I have a small penis' to change your settings: ")
        if(confirmation != ''):
            self.newUser()

        #TODO Production
        #print("Great! Remember you can chage your settings anytime by using the command 'leetline.exe changeUser'")


#Helper Functions Related to Program

## Check for the existance of pickles
def checkFlats():
    path = 'flats/' 
    if not os.path.exists(path):
        os.makedirs(path)

## print all commands available at the moment
def llhelp():
    print("The Help Function is Under Construction")
