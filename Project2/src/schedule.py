from settings import *
from input import *
from output import *
import random

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
                INCIDENCE[e1.id][e2.id] = False

# for x in EVENTS :
#     print(x.id, x.rooms)

# for x in INCIDENCE:
#     print(x)

class Slot:
    id = -1
    # event_room = {}
    # event_room[event_id] = room_id
    event_room = None

def getRandomSolution() :
    SLOTS = []
    for i in range (0, timeslots) :
        slot = Slot()
        slot.id = i
        slot.event_room = {}
        SLOTS.append(slot)

    available_events = EVENTS[:]
    while len(available_events) > 0:
        temp, slots = get_best_event(available_events, SLOTS)
        if len(slots) == 0:
            available_events = EVENTS[:]
            continue
        available_events.remove(temp)
        # slot = slots[random.randint(0, len(slots)-1)]
        slot_id = slots[0][0] #selects the slot with the biggest number of rooms

        SLOTS[slot_id].event_room[temp.id] = slots[0][2][random.randint(0, len(slots[0][2])-1)]

    return SLOTS

    
def get_best_event(available_events, SLOTS) :
    temp = {}
    for event in available_events :
        temp[event] = get_possible_slots(event, SLOTS)
    best_value = len(min(temp.values(), key=lambda x: len(x)))
    
    temp_list = []
    for event, value in temp.items() :
        if len(value) == best_value :
            temp_list.append(event)
    
    ret_index = random.randint(0,len(temp_list)-1)
    return temp_list[ret_index], temp[temp_list[ret_index]]

def get_possible_slots(event, SLOTS):
    # each elements is [slot id, current number os events, [available rooms id]]
    ret = []
    for slot in SLOTS:
        flag = True
        events = slot.event_room.keys()
        rooms = slot.event_room.values()
        if not all(r in rooms for r in event.rooms):
            for event_id in events:
                if not INCIDENCE[event.id][EVENTS[event_id].id]:
                    flag = False
            
            if flag:
                ret.append([slot.id, len(events), list(set(event.rooms)-set(list(rooms)))])

    ret.sort(key=lambda x: x[1], reverse=True)
    return ret


s = getRandomSolution()

for x in s:
    print(x.id, x.event_room)

write_to_file(s, num_events)

# print(filename)
# print(timeslots)
