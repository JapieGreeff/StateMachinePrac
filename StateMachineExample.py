# the state machine pattern is a way for us to decouple the decision making rules from the actions that the code will perform based on selected action. 

# let us first create a base class
class State:
    def __init__(self):
        pass

    def speak(self):
        pass

    def animation(self):
        pass

    def other_functionality(self):
        print('this is some default functionality')

# each state we are interested in gets derived from this base class
class SleepState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am sleeping')
        pass

    def animation(self):
        print('Play sleep animation')
        pass

class BreakfastState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am eating breakfast')
        pass

    def animation(self):
        print('Play breakfast animation')
        pass

class GymState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am at the gym')
        pass

    def animation(self):
        print('Play gym animation')
        pass

class ClassState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am in class')
        pass

    def animation(self):
        print('Play class animation')
        pass
    
class LunchState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am eating lunch')
        pass

    def animation(self):
        print('Play lunch animation')
        pass
    
class WatchTvState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am watching television')
        pass

    def animation(self):
        print('Play television animation')
        pass

class DinnerState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am eating dinner')
        pass

    def animation(self):
        print('Play dinner animation')
        pass

class RiverState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am relaxing by the river')
        pass

    def animation(self):
        print('Play river animation')
        pass

class ChurchState(State):
    def __init__(self):
        super().__init__()
        pass

    def speak(self):
        print('I am in church')
        pass

    def animation(self):
        print('Play church animation')
        pass