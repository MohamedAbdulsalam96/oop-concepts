#this is challange 9.1
#To practice OOP Concepts..
#####################################
class Animals:
    def init(self): ###### constractor
        self.__eat()

    def __del__(self):    ####### Destructor
        print("Animals class is Destructed")

    def eat(self):   #######private function
        print("All animals need food")

    def _Type(self,animalType): ####### protect function
        self.animalType=animalType
        print(f"i am {self.animalType} i have leather")

#***********************************************************
#***********************************************************

    #inhertance multilevel...........
class WildAnimals(Animals):    #######Class Child (1)..

    def __init__(self):  ####### constractor
        print("Welcome in Wild Animals Class " )

    def Placeliving(self):  #######abstract function in abstract class
        print("We are animals, they live in water.. ")


# ***********************************************************
# ***********************************************************
    # use get and set functions for encapslution
    # Encapslution....
    def setFeet(self,feet ):
        self.feet = feet

    def getFeet(self):       #######Encapslution
        print(f"it has {self.feet} feet.. ")


#***********************************************************
#***********************************************************

class  lion(WildAnimals):  #######Class Child (1)..
    print("I am the lion belongs to the wild animals class")
    def voice(self, animalName,ability):
        self.animalName = animalName
        self.ability = ability
        print(f"This Anmail named is {animalName} It is characterized by {self.ability}")


    def Placeliving(self):  ####### reuse abstract method
        print("We live in the woods ")

# ***********************************************************
# ***********************************************************
        ####### creat objects from classes.....

lionObj=lion()
lionObj.ability="every Things"
lionObj.Placeliving()
lionObj.animalName='mohamed'
lionObj.voice('mohamed',"power")
