from settings import *

input_file = open(filename + ".tim", "r")

first_line = input_file.readline().split()
num_events = int(first_line[0])
num_rooms = int(first_line[1])
num_features = int(first_line[2])
num_students = int(first_line[3])

rooms = []
for i in range(0, num_rooms):
    rooms.append(int(input_file.readline()))


# students_events[student][event]
# if 0 the students does not attend the event
# if 1 the students attends the event
students_events = []
for i in range(0, num_students):
    events_temp = []
    for j in range(0, num_events):
        num = int(input_file.readline())
        events_temp.append(num)
    students_events.append(events_temp)


# rooms_features[room][feature]
# if 0 the room does not satisfy the feature
# if 1 the room satisfies the feature
rooms_features = []
for i in range(0, num_rooms):
    features_temp = []
    for j in range(0, num_features):
        features_temp.append(int(input_file.readline()))
    rooms_features.append(features_temp)


# events_features[event][feature]
# if 0 the event does not require the feature
# if 1 the event requires the feature
events_features = []
for i in range(0, num_events):
    features_temp = []
    for j in range(0, num_features):
        features_temp.append(int(input_file.readline()))
    events_features.append(features_temp)
