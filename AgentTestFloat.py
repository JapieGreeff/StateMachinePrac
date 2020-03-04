from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Agent:

    def __init__(self, initialstate):
        self.state = initialstate
        pass

    def sense_world(self, dt, sick):
        self.state = self
        if((dt.weekday() >= 0 and dt.weekday() < 6)  and dt.hour == 6 and sick == False):
             self.state = Action.Breakfast
     
        elif((dt.weekday() == 6) or (dt.weekday() == 7)) and (dt.hour == 9 and sick == False):
          self.state = Action.Breakfast    
          
        elif(dt.weekday() < 5  and dt.hour == 7 and dt.hour < 8 and sick == False):
            self.state = Action.Gym
            
        elif(dt.weekday() > 6 and dt.hour() == 10 and sick == False):
           self.state = Action.Church
           
        elif(dt.weekday() < 5 and dt.hour >= 9 and dt.hour < 13 and sick == False):
                  self.state = Action.Class
           
        elif(dt.weekday() < 5 and dt.hour == 13 and dt.hour <= 14 and sick == False):
            self.state = Action.Lunch
            
        elif(dt.weekday() == 5 or dt.weekday() == 6 and dt.hour >  11 and dt.hour < 14 and sick == False):
           self.state = Action.River 
           
        elif(dt.weekday() < 5 and dt.hour >= 14 and dt.hour < 17 and sick == False):
                  self.state = Action.Class    
                 
        elif(dt.weekday() < 5 and dt.hour >= 17 and dt.hour < 19 and sick == False):
                  self.state = Action.Television
                 
        elif(dt.weekday() < 5 and dt.hour >= 19 and dt.hour < 20 and sick == False):
                  self.state = Action.Dinner            
            
        elif(dt.weekday() == 5 or dt.weekday() == 6 and dt.hour >= 14 and dt.hour < 19 and sick == False):
              self.state = Action.River 
            
        elif(dt.weekday() >= 0 and  dt.weekday() <= 6 and dt.hour >= 20 and dt.hour < 22 and sick == False):
           self.state = Action.Television     
           
        elif(dt.weekday() >= 0 and  dt.weekday() <= 6 and dt.hour >= 22 and dt.hour < 6 and sick == False):
           self.state = Action.Sleep
           
#        elif(dt.weekday() >= 0 and  dt.weekday() <= 6 and dt.hour >= 22 and dt.hour < 6 and sick == True):
#           self.state = Action.Dinner  
#         
#        elif(dt.weekday() >= 0 and  dt.weekday() <= 6 and dt.hour >= 22 and dt.hour < 6 and sick == False):
#           self.state = Action.Sleep    
         
#            
           
        return self.state
        #   first decide what state you should be in when the details of the environment are known, then set self.state to that
    # if xyz:
        #   self.state = Action.xyz
               
    
    def perform_action(self):
        if self.state == Action.Breakfast:
            return "I am eating breakfast"
        
        elif  self.state == Action.Lunch:
            return "I am eating lunch"
     
        elif  self.state == Action.Dinner:
           return "I am eating dinner"
         
        elif  self.state == Action.Sleep:
            return "I am sleeping"
        
        elif  self.state == Action.Gym:
            return "I am at the gym"
     
        elif  self.state == Action.Class:
            return "I am in class"
       
        elif  self.state == Action.Church:
            return "I am at church"
        
        elif  self.state == Action.Television:
            return "I am watching television"
        
        elif  self.state == Action.River:
           return "I am next to the river"
