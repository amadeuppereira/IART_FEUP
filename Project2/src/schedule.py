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
    num_students = 0
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

for event in EVENTS :
    for student in STUDENTS :
        if event.id in student.events :
            event.num_students += 1
    event.rooms = []
    for room in ROOMS :
        if (room.size >= event.num_students) and (set(event.features).issubset(set(room.features))):
            event.rooms.append(room.id)

for event in EVENTS :
    print(event.id, event.features, event.num_students, event.rooms)

# print(filename)
# print(timeslots)