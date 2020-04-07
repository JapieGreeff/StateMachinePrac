from datetime import datetime
from enum import Enum, IntEnum

#weekday = datetime.today().weekday()
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
       weekday = dt.weekday()
       dt.hour
        if (sick == False):
            if weekday == 0 and dt.hour == 6:
               
            if (dt.strptime("Monday", "%A") == "Monday" or dt.strptime("Wednesday", "%A") == "Wednesday" or dt.strptime(
                    "Friday", "%A") == "Friday"):
                if (dt.strptime("06", "%H") ==6 ):
                    self.state = Action.Breakfast
                elif (dt.strptime("07", "%H") == 7):
                    self.state = Action.Gym
                elif (dt.strptime("08", "%H") >= 8 and dt.strptime("%H") <=12 or dt.strptime("14", "%H") >= 14 and dt.strptime("16", "%H") <= 16):
                    self.state = Action.Class
                elif (dt.strptime("13", "%H") == 13):
                    self.state = Action.Lunch
                elif (dt.strptime("17", "%H") == 17 or dt.strptime("18", "%H") == 18):
                    self.state = Action.Television
                elif (dt.strptime("19", "%H") == 19):
                    self.state = Action.Dinner
                elif (dt.strptime("21", "%H") == 20 or dt.strptime("21", "%H") == 21):
                    self.state = Action.Television
                else:
                    self.state = Action.Sleep

        elif (dt.strptime("Tuesday", "%A") == "Tuesday" or dt.strptime("Thursday", "%A") == "Thursday"):
            if (dt.strptime("06", "%H") == 6 or dt.strptime("07", "%H") == 7):
                self.state = Action.Breakfast
            elif (dt.strptime("08","%H") >= 8 and dt.strptime("12","%H") <= 12 or dt.strptime("%H") >= 14 and dt.strptime("16","%H") <= 16):
                self.state = Action.Class
            elif (dt.strptime("13","%H") == 13):
                self.state = Action.Lunch
            elif (dt.strptime("17","%H") == 17 or dt.strptime("18","%H") == 18):
                self.state = Action.Television
            elif (dt.strptime("19","%H") == 19):
                self.state = Action.Dinner
            elif (dt.strptime("20","%H") == 20 or dt.strptime("21","%H") == 21):
                self.state = Action.Television
            else:
                self.state = Action.Sleep

        elif (dt.strptime("Saturday", "%A") == "Saturday"):
            if (dt.strptime("09","%H") == 9):
                self.state = Action.Breakfast
            elif (dt.strptime("10","%H") >= 10 and dt.strptime("13","%-") <= 13 or dt.strptime("15","%H") >= 15 and dt.strptime("18","%H") <= 18):
                self.state = Action.River
            elif (dt.strptime("14","%H") == 14):
                self.state = Action.Lunch
            elif (dt.strptime("19","%H") == 19):
                self.state = Action.Dinner
            elif (dt.strptime("20","%H") == 20 or dt.strptime("21","%H") == 21):
                self.state = Action.Television
            else:
                self.state = Action.Sleep

        elif (dt.strptime("Sunday", "%A") == "Sunday"):
            if (dt.strptime("09","%H") == 9):
                self.state = Action.Breakfast
            elif (dt.strptime("10","%H") == 10):
                self.state = Action.Church
            elif (dt.strptime("11","%H") >= 11 and dt.strptime("13","%H") <= 13 or dt.strptime("15","%H") >= 15 and dt.strptime("18","%H") <= 18):
                self.state = Action.River
            elif (dt.strptime("14","%H") == 14):
                self.state = Action.Lunch 
            elif (dt.strptime("19","%H") == 19):
                self.state = Action.Dinner
            elif (dt.strptime("20","%H") == 20 or dt.strptime("21","%H") == 21):
                self.state = Action.Television
            else:
                self.state = Action.Sleep

        elif (sick == True):
            if (dt.strptime("Monday", "%A") == "Monday" or dt.strptime("Tuesday", "%A") == "Tuesday" or dt.strptime(
                    "Wednesday", "%A") == "Wednesday" or dt.strptime("Thursday", "%A") == "Thursday" or dt.strptime(
                    "Friday", "%A") == "Friday"):
                if (dt.strptime("06", "%H") == 6):
                    self.state = Action.Breakfast
                elif (dt.strptime("13", "%H") == 13):
                    self.state = Action.Lunch
                elif (dt.strptime("19", "%H") == 19):
                    self.state = Action.Dinner
                else:
                    self.state = Action.Sleep
            else:
                if (dt.strptime("09", "%H") == 9):
                    self.state = Action.Breakfast
                elif (dt.strptime("14", "%H") == 14):
                    self.state = Action.Lunch
                elif (dt.strptime("19", "%H") == 19):
                    self.state = Action.Dinner
                else:
                    self.state = Action.Sleep
        return self.state

    def perform_action(self):
        if (self.state == Action.Breakfast):
            return "I am eating breakfast"
        elif (self.state == Action.Lunch):
            return "I am eating lunch"
        elif (self.state == Action.Dinner):
            return "I am eating dinner"
        elif (self.state == Action.Sleep):
            return "I am sleeping"
        elif (self.state == Action.Gym):
            return "I am at the gym"
        elif (self.state == Action.Class):
            return "I am in class"
        elif (self.state == Action.Church):
            return "I am at church"
        elif (self.state == Action.Television):
            return "I am watching television"
        elif (self.state == Action.Lunch):
            return "I am next to the river"
