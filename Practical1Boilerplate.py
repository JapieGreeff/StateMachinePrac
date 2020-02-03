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

    def sense_world(self, dt):
        # first decide what state you should be in when the details of the environment are known, then set self.state to that
        # if xyz:
        #   self.state = Action.xyz
        return self.state

    def perform_action(self):
        if self.state == Action.Breakfast:
            return "I am eating breakfast"
        # add in the logic for all the other states
        # return "I am eating lunch"
        # return "I am eating dinner"
        # return "I am sleeping"
        # return "I am at the gym"
        # return "I am in class"
        # return "I am at church"
        # return "I am watching television"
        # return "I am next to the river"


testAgent = Agent(Action.Breakfast)

d1 = datetime(year = 2020, month = 2, day = 25, hour = 15, minute = 55, second = 59)

testAgent.sense_world(d1)
print(testAgent.perform_action())
