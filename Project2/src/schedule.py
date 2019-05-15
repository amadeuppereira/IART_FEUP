from settings import *
from input import *
from output import *

class Room:
    id = -1
    size = 0
    features = None

class Student:
    id = -1
    events = None

class Event:
    id = -1
    features = None
    students = None
    rooms = None

ROOMS = []
STUDENTS = []
EVENTS = []

for i, size in enumerate(rooms):
    r = Room()
    r.id = i
    r.size = size
    ROOMS.append(r)
    
for i, events in enumerate(students_events):
    s = Student()
    s.id = i
    s.events = []
    for j, event in enumerate(events):
        if event:
            s.events.append(j)
    STUDENTS.append(s)

for i, features in enumerate(rooms_features):
    ROOMS[i].features = []
    for j, feature in enumerate(features):
        if(feature):
            ROOMS[i].features.append(j)

for i, features in enumerate(events_features):
    e = Event()
    e.id = i
    e.features = []
    for j, feature in enumerate(features):
        if feature:
            e.features.append(j)
    EVENTS.append(e)

# Get possible rooms for all events
for event in EVENTS :
    event.students = []
    for student in STUDENTS :
        if event.id in student.events :
            event.students.append(student.id)

    event.rooms = []
    for room in ROOMS :
        if (room.size >= len(event.students)) and (set(event.features).issubset(set(room.features))):
            event.rooms.append(room.id)

INCIDENCE = [[False for x in range(len(EVENTS))] for y in range(len(EVENTS))]

for e1 in EVENTS:
    for e2 in EVENTS:
        if not any(s in e2.students for s in e1.students):
            INCIDENCE[e1.id][e2.id] = True

for e1 in EVENTS:
    if len(e1.rooms) == 1:
        for e2 in EVENTS:
            if len(e2.rooms) == 1 and e1.rooms[0] == e2.rooms[0]:
                INCIDENCE[e1.id][e2.id] == False


# print(filename)
# print(timeslots)
