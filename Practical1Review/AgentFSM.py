from datetime import datetime
from StateMachineExample import *

class Agent:

    def __init__(self, initialstate):
        # ignoring the initialisation - set to None
        self.state = State(initialstate)
        
    def sense_world(self, dt, sick):
        self.state = self.state.set_state(dt, sick)
        return self.state.get_state()

    def perform_action(self):
        return self.state.speak()



