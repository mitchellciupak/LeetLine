#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import sys
import pickle
from program import Program


## TODO Need Categories like Trees or Something 

class Problem: 
    #Unflatten Class
    def load(self):
        f = open("flats/prob" + str(self.id) + ".pickle","rb")
        tmp_dict = pickle.load(f)
        f.close()          
        self.__dict__.update(tmp_dict) 

    #Flatten Class
    def save(self):
        f = open("flats/prob" + str(self.id) + ".pickle","wb")
        pickle.dump(self.__dict__, f, 2)
        f.close()

    def __init__(self, id):
        self.prog = Program() #TODO May just want to inherrit prog
        self.id = id
        try: 
            self.load()
        except:    
            self.createNewProblem()

    def __del__(self):
        self.save()

    # Method creates the template to implament and slove a problem
    def createNewProblem(self): 
        self.name = input("1. Please enter the problem name: ")
        self.source = input("2. Please enter a link or description of the source: ") 
        self.dateTimeCreated = self.prog.getDateTime()

        self.filename = ''.join(word.title() for word in self.name.split(' '))

        #TODO Debug
        self.foldername = "C:/leetline" + "/" + self.filename + "/" + self.filename
        #self.foldername = self.prog.getPrefDirectory() + "/" + self.filename + "/" + self.filename

        #Create Project File
        if(self.prog.getPrefLanguage == 'Python'):
            fptr = open(self.filename + ".py","w+")
            fptr.write("Write in basic template with descripion and everything")
            fptr.close()