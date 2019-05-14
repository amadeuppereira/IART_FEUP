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



# print(filename)
# print(timeslots)