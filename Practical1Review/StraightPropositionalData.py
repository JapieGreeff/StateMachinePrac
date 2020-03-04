from datetime import datetime

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

print('Logic output:')
print(get_action_propositional_logic(d1, False))
print(get_action_propositional_logic(d1, True))
print(get_action_propositional_logic(d2, False))
print(get_action_propositional_logic(d2, True))
print(get_action_propositional_logic(d3, False))
print(get_action_propositional_logic(d3, True))