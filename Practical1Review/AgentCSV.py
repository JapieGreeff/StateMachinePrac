from datetime import datetime
from enum import Enum, IntEnum
import pandas as pd
import numpy as np

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
        self.df = pd.read_csv('Calendar.csv', index_col=0)
        self.dfsick = pd.read_csv('CalendarSick.csv', index_col=0)
        

    def sense_world(self, dt, sick):
        dow = dt.weekday()
        hour = dt.hour
        if not sick:
            value = df.get_value(dow, hour, takeable = True)
            self.state = Action[value]
        else:
            value = dfsick.get_value(dow, hour, takeable = True)
            self.state = Action[value]
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





# reading from the csv file we want the index column to be the row names we have in the csv file representing days of the week
df = pd.read_csv('Calendar.csv', index_col=0)
#print(df)

# our dataframe now contains our full calendar. In order to see the action we should take at a particular point in time, we can use it as a lookup table 
def performAction(day, time):
    return df.at[day,time]

print('testing lookup')
print(performAction('Monday','1:00'))
print(performAction('Tuesday','11:00'))
print(performAction('Wednesday','7:00'))
print(performAction('Sunday','10:00'))

# This however gets problematic when we include the proviso that if you are sick, then you will stay in bed unless it's mealtime. A simple lookup now doesn't work anymore.
# what we can do however, is to create a second lookup calendar which will be used in the event that the student is sick
df = pd.read_csv('Calendar.csv', index_col=0)
dfsick = pd.read_csv('CalendarSick.csv', index_col=0)
def performActionSickCheck(sick, day, time):
    if not sick:
        return df.at[day,time]
    else:
        return dfsick.at[day,time]