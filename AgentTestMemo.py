from Agent import Action, Agent
from datetime import datetime
from enum import Enum, IntEnum

# create the test agent
testAgent = Agent(Action.Breakfast)

# send the agent the details of the environment
testdatetimes = []
#monday
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 4, minute = 55, second = 59), Action.Sleep, "I am sleeping"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 6, minute = 55, second = 59), Action.Breakfast, "I am eating breakfast"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 7, minute = 55, second = 59), Action.Gym, "I am at the gym"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 9, minute = 55, second = 59), Action.Class, "I am in class"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 13, minute = 55, second = 59), Action.Lunch, "I am eating lunch"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 15, minute = 55, second = 59), Action.Class, "I am in class"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 17, minute = 55, second = 59), Action.Television, "I am watching television"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 19, minute = 55, second = 59), Action.Dinner, "I am eating dinner"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 21, minute = 55, second = 59), Action.Television ,"I am watching television"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 3, hour = 23, minute = 55, second = 59), Action.Sleep, "I am sleeping"))
# Tuesday
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 4, minute = 55, second = 59), Action.Sleep, "I am sleeping"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 6, minute = 55, second = 59), Action.Breakfast, "I am eating breakfast"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 9, minute = 55, second = 59), Action.Class, "I am in class"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 13, minute = 55, second = 59), Action.Lunch, "I am eating lunch"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 15, minute = 55, second = 59), Action.Class, "I am in class"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 17, minute = 55, second = 59), Action.Television, "I am watching television"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 19, minute = 55, second = 59), Action.Dinner, "I am eating dinner"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 21, minute = 55, second = 59), Action.Television ,"I am watching television"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 4, hour = 23, minute = 55, second = 59), Action.Sleep, "I am sleeping"))
# saturday
testdatetimes.append((datetime(year = 2020, month = 2, day = 8, hour = 9, minute = 55, second = 59), Action.Breakfast, "I am eating breakfast"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 8, hour = 10, minute = 55, second = 59), Action.River, "I am next to the river"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 8, hour = 14, minute = 55, second = 59), Action.Lunch, "I am eating lunch"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 8, hour = 19, minute = 55, second = 59), Action.Dinner, "I am eating dinner"))
# sunday
testdatetimes.append((datetime(year = 2020, month = 2, day = 9, hour = 9, minute = 55, second = 59), Action.Breakfast, "I am eating breakfast"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 9, hour = 10, minute = 55, second = 59), Action.Church, "I am at church"))
testdatetimes.append((datetime(year = 2020, month = 2, day = 8, hour = 11, minute = 55, second = 59), Action.River, "I am next to the river"))

totalPossibleMarks = 0
correct = 0
# healthy tests
for i in testdatetimes:
    totalPossibleMarks = totalPossibleMarks + 3
    agentState = testAgent.sense_world(i[0], False)
    print(f'wanted:{i[1]} got: {agentState}')
    if agentState == i[1]:
        correct = correct + 2
    if testAgent.perform_action() == i[2]:
        correct = correct + 1

# sick tests
for i in testdatetimes:
    totalPossibleMarks = totalPossibleMarks + 2
    agentState = testAgent.sense_world(i[0], True)
    testState = i[1]
    if not (testState == Action.Breakfast or testState == Action.Lunch or testState == Action.Dinner):
        testState = Action.Sleep
    print(f'wanted:{testState} got: {agentState}')
    if agentState == testState:
        correct = correct + 2

print (f"Final mark: {correct}/{totalPossibleMarks} = {100*correct/totalPossibleMarks}")
