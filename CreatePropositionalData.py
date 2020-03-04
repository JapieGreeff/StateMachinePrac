import pandas as pd
import numpy as np

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

print('testing sick test lookup')
print(performActionSickCheck(False, 'Monday','1:00'))
print(performActionSickCheck(False, 'Tuesday','11:00'))
print(performActionSickCheck(False, 'Wednesday','7:00'))
print(performActionSickCheck(False, 'Sunday','10:00'))
print(performActionSickCheck(True, 'Monday','1:00'))
print(performActionSickCheck(True, 'Tuesday','11:00'))
print(performActionSickCheck(True, 'Wednesday','7:00'))
print(performActionSickCheck(True, 'Sunday','10:00'))
print(performActionSickCheck(True, 'Sunday','14:00'))

# this assumes however that we will only be using time values that are on the hour every hour. What happens if we now want to look at the calendar at say 13:47?
# now a lookup won't work at all and we will need to have a number of logical tests to see what time of day we should be lookin up in our calendar

# Your schedule is as shown in the weekly calender

# You Sleep till 6AM each weekday when you get up
# You Sleep till 9AM on the weekend when you get up
# First thing you do when you get up is to eat Breakfast
# On mondays, wednesdays and fridays you go to the Gym for an hour after Breakfast
# On sundays you go to Church after Breakfast for an hour
# After Breakfast and Gym (if relevant) you go to Class on weekdays till 1PM when you break for Lunch
# On saturdays and sundays you go to the River after Breakfast and Church till Lunch at 2PM
# After Lunch on a weekday you go back to Class till 5PM when you go home and watch some television
# After Lunch on a weekend day you go back to the River till Dinner at 7PM
# Every day you stop what you are doing and eat Dinner at 7PM
# Every day after you eat Dinner you watch some television till 10PM when you go to bed. 
from datetime import datetime
from enum import Enum, IntEnum

class Action(IntEnum):
    Sleep = 1
    Breakfast = 2
    Gym = 3
    Class = 4
    Lunch = 5
    Television = 6
    Dinner = 7
    River = 8
    Church = 9

# for our purposes, we only care about the day of the week, sickness and the hour. 
def get_action(dt, sickness):
    dow = dt.weekday()
    hour = dt.hour
    if (hour == 6 and dow <= 4) or (hour == 9 and dow >= 5):
        return Action.Breakfast
    elif (hour == 13 and dow <= 4) or (hour == 14 and dow >= 5):
        return Action.Lunch
    elif hour == 19:
        return Action.Dinner
    elif sickness or hour < 6 or (hour < 9 and dow >= 5) or hour >= 22:
        return Action.Sleep
    elif hour == 7 and (dow == 0 or dow == 2 or dow == 4):
        return Action.Gym
    elif hour < 17 and dow <= 4:
        return Action.Class    
    elif hour == 10 and dow == 6:
        return Action.Church
    elif hour >= 20 or dow <= 4:  # notice how this is the last action left in the weekdays- otherwise other rules would have triggered
        return Action.Television
    else:
        return Action.River

# this approach works, but the order of the rules, and not just the rules is now important - see how the last 2 are "remainders" after other rules have triggered.  

# datetime(year, month, day, hour, minute, second, microsecond)
d1 = datetime(2020, 1, 25, 15, 55, 59, 0)
d2 = datetime(2020, 1, 13, 11, 1, 23, 0)
d3 = datetime(2020, 1, 13, 6, 1, 23, 0)
print(get_action(d1, False))
print(get_action(d1, True))
print(get_action(d2, False))
print(get_action(d2, True))
print(get_action(d3, False))
print(get_action(d3, True))

# This works, but what now if we need to add in more functions for other actions/features. For example, speak, animation and location?
def speak(action):
    if action == Action.Sleep:
        print('I am Sleeping')
    if action == Action.Breakfast:
        print('I am eating Breakfast')
    if action == Action.Gym:
        print('I am at the Gym')
    if action == Action.Class:
        print('I am in Class')
    if action == Action.Lunch:
        print('I am eating Lunch')
    if action == Action.Television:
        print('I am watching television')
    if action == Action.Dinner:
        print('I am eating Dinner')
    if action == Action.River:
        print('I am relaxing by the River')
    if action == Action.Church:
        print('I am in Church')

def animation(action):
    if action == Action.Sleep:
        print('Play Sleep animation')
    if action == Action.Breakfast:
        print('Play Breakfast animation')
    if action == Action.Gym:
        print('Play Gym animation')
    if action == Action.Class:
        print('Play Class animation')
    if action == Action.Lunch:
        print('Play Lunch animation')
    if action == Action.Television:
        print('Play television animation')
    if action == Action.Dinner:
        print('Play Dinner animation')
    if action == Action.River:
        print('Play River animation')
    if action == Action.Church:
        print('Play Church animation')

speak(get_action(d1, False))
speak(get_action(d1, True))
animation(get_action(d1, False))
animation(get_action(d1, True))
speak(get_action(d2, False))
speak(get_action(d2, True))
animation(get_action(d2, False))
animation(get_action(d2, True))
speak(get_action(d3, False))
speak(get_action(d3, True))
animation(get_action(d3, False))
animation(get_action(d3, True))

# The problem now, is what happens when something changes? We have all of our logic check split between different functions. What happens if we want
# to add in more detail to the schedule or change it? What happens if we change the Enum? What happens if we want to add in another kind of action?
# let us explore a different design pattern that may simplify this work for us a little, and then combine it with a simple machine learning algorithm
# to remove the burden of some of the code writing. 
print('testing state machines')
from StateMachineExample import *

# for our purposes, we only care about the day of the week, sickness and the hour. 
def get_state(dt, sickness):
    dow = dt.weekday()
    hour = dt.hour
    if (hour == 6 and dow <= 4) or (hour == 9 and dow >= 5):
        return BreakfastState()
    if (hour == 13 and dow <= 4) or (hour == 14 and dow >= 5):
        return LunchState()
    if hour == 19:
        return DinnerState()
    if sickness or hour < 6 or (hour < 9 and dow >= 5) or hour >= 22:
        return SleepState()
    if hour == 7 and (dow == 0 or dow == 2 or dow == 4):
        return GymState()
    if hour < 17 and dow <= 4:
        return ClassState()    
    if hour == 10 and dow == 6:
        return ChurchState()
    if hour >= 20 or dow <= 4:  # notice how this is the last action left in the weekdays- otherwise other rules would have triggered
        return WatchTvState()
    else:
        return RiverState()


get_state(d1, False).speak()
get_state(d1, True).speak()
get_state(d1, False).animation()
get_state(d1, True).animation()
get_state(d2, False).speak()
get_state(d2, True).speak()
get_state(d2, False).animation()
get_state(d2, True).animation()
get_state(d3, False).speak()
get_state(d3, True).speak()
get_state(d3, False).animation()
get_state(d3, True).animation()

# this way, the speak and animation functions each belong with their state. To add in a new state when the enum changes we can just create a new state
# Class for that enum value and just write the new speak and animation code without having to change any other functions. additionally, you now have
# a base Class that can give default functionality

get_state(d1, False).other_functionality()
get_state(d1, True).other_functionality()
get_state(d2, False).other_functionality()
get_state(d2, True).other_functionality()
get_state(d3, False).other_functionality()
get_state(d3, True).other_functionality()

# with this state machine functionality, we only need to worry about the functionality that each state brings to the table, but we still need to decide
# what state we need to be in with the get_state function that we will need to change whenever the schedule changes. Machine learning however will allow
# us to automate this. 
# first we will use the dataframes we read from the csv files and create a dataset of the form: dow, hour, action. We need this for both healthy and sick versions.

print('creating decision tree classifier data set')

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
# get all the data for the normal calendar and put it into the training set and the label set
df = pd.read_csv('Calendar.csv', index_col=0)
columns = list(df)
for index, row in df.iterrows():
    for idcol, col in enumerate(columns): # enumerate gives us not only the objects we are enumerating over but also an index
        #print(f'{row.name}:{col}:{df[col][index]}')
        #print(f'{row.name}:{idcol}:{df[col][index]}')
        X.append([ int(Dow[index]), idcol, 0])
        y.append( int(Action[df[col][index]]))

# get all the data for the sick calendar and put it into the training set and the label set
dfsick = pd.read_csv('CalendarSick.csv', index_col=0)
columns = list(dfsick)
for index, row in dfsick.iterrows():
    for idcol, col in enumerate(columns): # enumerate gives us not only the objects we are enumerating over but also an index
        #print(f'{row.name}:{col}:{df[col][index]}')
        #print(f'{row.name}:{idcol}:{df[col][index]}')
        X.append([int(Dow[index]), idcol, 1])
        y.append( int(Action[dfsick[col][index]]))


# we now have Features in X and labels in y
for row in zip(X,y):
    print(row)

print('learning and plot of decision tree')
# from the tutorial here: https://scikit-learn.org/stable/modules/tree.html
import graphviz 
from sklearn import tree
decisionTree = tree.DecisionTreeClassifier()
decisionTree = decisionTree.fit(X, y)
# creates the tree in Dot format
dot_data = tree.export_graphviz(decisionTree, out_file=None, 
                                feature_names=['Day of week', 'Hour in day', 'Sick'], 
                                class_names=['Sleep','Breakfast','Gym','Class','Lunch','Television','Dinner','River','Church'],
                                filled=True, rounded=True, special_characters=True) 
graph = graphviz.Source(dot_data) 
# renders the decision tree as an image file 
graph.render("student schedule",  format='png') 

print('testing the decision tree')
print('Healthy')
print(f'[{Dow(d1.weekday()).name},{d1.hour}, 0] = {Action(decisionTree.predict([[d1.weekday(),d1.hour, 0]])[0]).name}')
print(f'[{Dow(d2.weekday()).name},{d2.hour}, 0] = {Action(decisionTree.predict([[d2.weekday(),d2.hour, 0]])[0]).name}')
print(f'[{Dow(d3.weekday()).name},{d3.hour}, 0] = {Action(decisionTree.predict([[d3.weekday(),d3.hour, 0]])[0]).name}')
print('Sick')
print(f'[{Dow(d1.weekday()).name},{d1.hour}, 1] = {Action(decisionTree.predict([[d1.weekday(),d1.hour, 1]])[0]).name}')
print(f'[{Dow(d2.weekday()).name},{d2.hour}, 1] = {Action(decisionTree.predict([[d2.weekday(),d2.hour, 1]])[0]).name}')
print(f'[{Dow(d3.weekday()).name},{d3.hour}, 1] = {Action(decisionTree.predict([[d3.weekday(),d3.hour, 1]])[0]).name}')
