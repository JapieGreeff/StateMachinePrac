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

# for our purposes, we only care about the day of the week, sickness and the hour. 
# this approach works, but the order of the rules, and not just the rules is now important - see how the last 2 are "remainders" after other rules have triggered.  
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

# let us now create a function that uses Propositional logic formally rather than implicitly
def get_action_propositional_logic(dt, sickness):
    dow = dt.weekday()  # integer
    hour = dt.hour      # integer
    # Let us split out the semantic layer - here we indicate what each proposition means and assign it a truth value (interpretation)
    A = hour == 6
    B = dow <= 4
    C = hour == 9
    D = dow >= 5
    E = hour == 13
    F = hour == 14
    G = hour == 19
    H = hour < 6
    I = hour < 9
    J = hour >= 22
    K = hour == 7
    L = dow == 0
    M = dow == 2
    N = dow == 4
    O = hour < 17
    P = hour == 10
    Q = dow == 6
    R = hour >= 20
    S = sickness
    
    # Once we have propositions with truth values, we use the operators to determine the truth values of the query formulas 
    O1 = (A and B) or (C and D) # Breakfast
    O2 = (E and B) or (F and D) # Lunch
    O3 = G # Dinner
    O4 = (S or H or (I and D) or J) and not O1 and not O2 and not O3 # Sleep when you aren't eating
    O5 = (K and (L or M or N)) and not O4 # Gym - sleep overrides
    O6 = (O and B) and not O1 and not O2 and not O3 and not O4 and not O5 # Class - because our predicate hour is < we have to lock out many other values
    O7 = (P and Q) and not O4  # Church - sleep overrides
    O8 = (R or B) and not O1 and not O2 and not O3 and not O4 and not O5 and not O6 and not O7 # Television - this is a catch all 
    O9 = not O1 and not O2 and not O3 and not O4 and not O5 and not O6 and not O7 and not O8  # River - the last remaining option is a catch all.
    # return the logic as a one hot array
    return O1, O2, O3, O4, O5, O6, O7, O8, O9

# datetime(year, month, day, hour, minute, second, microsecond)
d1 = datetime(2020, 1, 25, 15, 55, 59, 0)
d2 = datetime(2020, 1, 13, 11, 1, 23, 0)
d3 = datetime(2020, 1, 13, 6, 1, 23, 0)
print('Pythonic output:')
print(get_action(d1, False))
print(get_action(d1, True))
print(get_action(d2, False))
print(get_action(d2, True))
print(get_action(d3, False))
print(get_action(d3, True))

print('Logic output:')
print(get_action_propositional_logic(d1, False))
print(get_action_propositional_logic(d1, True))
print(get_action_propositional_logic(d2, False))
print(get_action_propositional_logic(d2, True))
print(get_action_propositional_logic(d3, False))
print(get_action_propositional_logic(d3, True))