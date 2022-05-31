from random import seed
from random import randint

class Person:
    def __init__ (self,age,mobility,geneticdefence):
        self.infected = False
        self.dead = False
        self.recovered = False
        self.age = age
        self.mobility = mobility
        self.geneticdefence = geneticdefence
        seed(1)
        
    def applyInfection (self, r):
        print( self.infected )
        
        # If infected do not process
        if( self.infected ):
            return
    
        # build person specific infection probability
        ageAddition = round(float((self.age / 100) * 30))
        mobilityAddition = round(float((self.mobility / 100) * 30))
        rAddition = round(float((r / 100) * 40))
        infectionProbability = ageAddition + mobilityAddition + rAddition
        
        print( "Infection Prob: ", infectionProbability)
        
        # Apply negatives
        infectionProbability -= self.geneticdefence
        if( self.recovered ):
            infectionProbability -= 20
            
        # Always must be a positive
        if( infectionProbability < 0 ):
            infectionProbability = 0
            
        # Decide whether infected
        if( randint(0,100) <= infectionProbability ):
            print("INFECTED")
            self.infected = True
        elif:
            print("NOT INFECTED")
