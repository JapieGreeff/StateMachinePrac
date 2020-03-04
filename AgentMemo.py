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
        dow = dt.weekday()
        hour = dt.hour
        if (hour == 6 and dow <= 4) or (hour == 9 and dow >= 5):
            self.state = Action.Breakfast
        elif (hour == 13 and dow <= 4) or (hour == 14 and dow >= 5):
            self.state = Action.Lunch
        elif hour == 19:
            self.state = Action.Dinner
        elif sick or hour < 6 or (hour < 9 and dow >= 5) or hour >= 22:
            self.state = Action.Sleep
        elif hour == 7 and (dow == 0 or dow == 2 or dow == 4):
            self.state = Action.Gym
        elif hour < 17 and dow <= 4:
            self.state = Action.Class    
        elif hour == 10 and dow == 6:
            self.state = Action.Church
        elif hour >= 20 or dow <= 4:  # notice how this is the last action left in the weekdays- otherwise other rules would have triggered
            self.state = Action.Television
        else:
            self.state = Action.River
        return self.state

    def perform_action(self):
        if self.state == Action.Breakfast:
            return "I am eating breakfast"
        if self.state == Action.Lunch:
            return "I am eating lunch"
        if self.state == Action.Dinner:
            return "I am eating dinner"
        if self.state == Action.Sleep:
            return "I am sleeping"
        if self.state == Action.Gym:
            return "I am at the gym"
        if self.state == Action.Class:
            return "I am in class"
        if self.state == Action.Church:
            return "I am at church"
        if self.state == Action.Television:
            return "I am watching television"
        if self.state == Action.River:
            return "I am next to the river"
