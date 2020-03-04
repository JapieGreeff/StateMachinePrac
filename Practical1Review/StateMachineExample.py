# the state machine pattern is a way for us to decouple the decision making rules from the actions that the code will perform based on selected action. 
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

# let us first create a base class
class State:
    def __init__(self, state):
        self.state = state
        pass

    def set_state(self, dt, sickness):
        dow = dt.weekday()
        hour = dt.hour
        if (hour == 6 and dow <= 4) or (hour == 9 and dow >= 5):
            return BreakfastState(Action.Breakfast)
        if (hour == 13 and dow <= 4) or (hour == 14 and dow >= 5):
            return LunchState(Action.Lunch)
        if hour == 19:
            return DinnerState(Action.Dinner)
        if sickness or hour < 6 or (hour < 9 and dow >= 5) or hour >= 22:
            return SleepState(Action.Sleep)
        if hour == 7 and (dow == 0 or dow == 2 or dow == 4):
            return GymState(Action.Gym)
        if hour < 17 and dow <= 4:
            return ClassState(Action.Class)    
        if hour == 10 and dow == 6:
            return ChurchState(Action.Church)
        if hour >= 20 or dow <= 4:  # notice how this is the last action left in the weekdays- otherwise other rules would have triggered
            return WatchTvState(Action.Television)
        else:
            return RiverState(Action.River)

    def get_state(self):
        return self.state

    def speak(self):
        pass

    def animation(self):
        pass


# each state we are interested in gets derived from this base class
class SleepState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am sleeping'

    def animation(self):
        return 'Play sleep animation'

class BreakfastState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am eating breakfast'

    def animation(self):
        return 'Play breakfast animation'

class GymState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am at the gym'

    def animation(self):
        return 'Play gym animation'

class ClassState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am in class'

    def animation(self):
        return 'Play class animation'
    
class LunchState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am eating lunch'

    def animation(self):
        return 'Play lunch animation'
    
class WatchTvState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am watching television'

    def animation(self):
        return 'Play television animation'

class DinnerState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am eating dinner'

    def animation(self):
        return 'Play dinner animation'

class RiverState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am next to the river'

    def animation(self):
        return 'Play river animation'

class ChurchState(State):
    def __init__(self, state):
        super().__init__(state)

    def speak(self):
        return 'I am at church'

    def animation(self):
        return 'Play church animation'