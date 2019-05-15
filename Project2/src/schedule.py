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
SLOTS = []

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
    for i in range (0, timeslots) :
        slot = Slot()
        slot.id = i
        slot.event_room = {}
        SLOTS.append(slot)

    # i = 0
    
    # while i < len(EVENTS) :
    #     print(i)
    #     room_id = EVENTS[i].rooms[random.randint(0,len(EVENTS[i].rooms)-1)]
    #     slot_id = random.randint(0,44)
    #     if room_id not in SLOTS[slot_id].event_room.values() :
    #         flag = True
    #         for event_slots in SLOTS[slot_id].event_room :
    #             if INCIDENCE[EVENTS[i].id][event_slots] == False :
    #                 flag = False
    #         if flag :
    #             SLOTS[slot_id].event_room[EVENTS[i].id] = room_id
    #             i += 1

    #         # SLOTS[random.randint(0,44)].event_room[EVENTS[i].id] = room_id
    #         # i += 1

    # SLOTS[0].event_room[EVENTS[3].id] = EVENTS[3].rooms[0]
    # SLOTS[2].event_room[EVENTS[2].id] = EVENTS[2].rooms[0]

    available_events = EVENTS[:]
    while len(available_events) > 0:
        temp, slots = get_best_event(available_events)
        available_events.remove(temp)
        slot = slots[random.randint(0, len(slots)-1)]        
        
        # print(temp.id)

def get_best_event(available_events) :
    temp = {}
    for event in available_events :
        temp[event] = get_possible_slots(event)
    best_value = min(temp.values(), key=lambda x: len(x))
    
    temp_list = []
    for event, value in temp.items() :
        if value == best_value :
            temp_list.append(event)
    
    ret_index = random.randint(0,len(temp_list)-1)
    return temp_list[ret_index], temp[temp_list[ret_index]]

def get_possible_slots(event):
    ret = []
    for slot in SLOTS:
        flag = True
        events = slot.event_room.keys()
        rooms = slot.event_room.values()
        if not all(r in rooms for r1 in event.rooms):
            for event_id in events:
                if not INCIDENCE[event.id][EVENTS[event_id].id]:
                    flag = False
                    break
        
        if flag:
            ret.append(slot.id)

    return ret
        
            
getRandomSolution()
# # print(INCIDENCE[0])
# SLOTS[0].event_room[EVENTS[3].id] = EVENTS[3].rooms[0]
# SLOTS[2].event_room[EVENTS[2].id] = EVENTS[2].rooms[0]
# print(get_possible_slots(EVENTS[0]))

        


# getRandomSolution()

# for x in SLOTS:
#     print(x.id, x.event_room)


# print(filename)
# print(timeslots)
