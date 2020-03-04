from datetime import datetime
from enum import Enum, IntEnum
import pandas as pd
import numpy as np
from sklearn import tree

class Action(Enum):
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
        # create an intEnum so that we can cast it to an integer for the training data
        class IntAction(IntEnum):
            Breakfast = 1
            Lunch = 2
            Dinner = 3
            Sleep = 4
            Gym = 5
            Class = 6
            Church = 7
            Television = 8
            River = 9

        # create an intEnum so that we can cast it to an integer for the training data
        class Dow(IntEnum):
            Monday = 0
            Tuesday = 1
            Wednesday = 2
            Thursday = 3
            Friday = 4
            Saturday = 5
            Sunday = 6

        X = []
        y = []
        # get all the data for the normal calendar and put it into the training set and the label set as rows
        df = pd.read_csv('Calendar.csv', index_col=0)
        columns = list(df)
        for index, row in df.iterrows():
            for idcol, col in enumerate(columns): # enumerate gives us not only the objects we are enumerating over but also an index
                X.append([ int(Dow[index]), idcol, 0])
                y.append( int(IntAction[df[col][index]]))

        # get all the data for the sick calendar and put it into the training set and the label set as rows
        dfsick = pd.read_csv('CalendarSick.csv', index_col=0)
        columns = list(dfsick)
        for index, row in dfsick.iterrows():
            for idcol, col in enumerate(columns): # enumerate gives us not only the objects we are enumerating over but also an index
                X.append([int(Dow[index]), idcol, 1])
                y.append( int(IntAction[dfsick[col][index]]))
        
        self.decisionTree = tree.DecisionTreeClassifier()
        self.decisionTree = self.decisionTree.fit(X, y)
        self.state = initialstate
        
    def sense_world(self, dt, sick):
        if not sick:
            self.state = Action(self.decisionTree.predict([[dt.weekday(),dt.hour, 0]])[0])
        else:
            self.state = Action(self.decisionTree.predict([[dt.weekday(),dt.hour, 1]])[0])
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
