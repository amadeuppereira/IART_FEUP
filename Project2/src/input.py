from settings import FILENAME

class Room:
    def __init__(self, id, size, features = None):
        self.id = id
        self.size = size
        self.features = features if features else []
    
    def addFeature(self, feature):
        self.features.append(feature)
        
class Student:
    def __init__(self, id, events = None):
        self.id = id
        self.events = events if events else []
        
    def addEvent(self, event):
        self.events.append(event)

class Event:
    def __init__(self, id, features = None):
        self.id = id
        self.features = features if features else []
    
    def addFeature(self, feature):
        self.features.append(feature)

ROOMS = []
STUDENTS = []
EVENTS = []

# ----- ----- ----- ----- ----- ----- ----- ----- -----

input_file = open(FILENAME + ".tim", "r")

first_line = input_file.readline().split()
num_events = int(first_line[0])
num_rooms = int(first_line[1])
num_features = int(first_line[2])
num_students = int(first_line[3])

# parse room size
for i in range(0, num_rooms):
    r = Room(i, int(input_file.readline()))
    ROOMS.append(r)

# parse student/event info
for i in range(0, num_students):
    s = Student(i)
    for j in range(0, num_events):
        if int(input_file.readline()):
            s.addEvent(j)
    STUDENTS.append(s)

# parse room/feature info
for i in range(0, num_rooms):
    for j in range(0, num_features):
        if int(input_file.readline()):
            ROOMS[i].addFeature(j)

# parse event/feature info
for i in range(0, num_events):
    e = Event(i)
    for j in range(0, num_features):
        if int(input_file.readline()):
            e.addFeature(j)
    EVENTS.append(e)