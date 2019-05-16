import numpy as np
from settings import *
from input import *
from output import *
import random
import copy as cp


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
for event in EVENTS:
    event.students = []
    for student in STUDENTS:
        if event.id in student.events:
            event.students.append(student.id)

    event.rooms = []
    for room in ROOMS:
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

def get_best_event(available_events, SLOTS):
    temp = {}
    for event in available_events:
        temp[event] = get_possible_slots(event, SLOTS)
    best_value = len(min(temp.values(), key=lambda x: len(x)))

    temp_list = []
    for event, value in temp.items():
        if len(value) == best_value:
            temp_list.append(event)

    ret_index = random.randint(0, len(temp_list)-1)
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
                ret.append([slot.id, len(events), list(
                    set(event.rooms)-set(list(rooms)))])

    ret.sort(key=lambda x: x[1], reverse=True)
    return ret

def getRandomSolution():
    SLOTS = []
    for i in range(0, timeslots):
        slot = Slot()
        slot.id = i
        slot.event_room = {}
        SLOTS.append(slot)

    available_events = EVENTS[:]
    while len(available_events) > 0:
        temp, slots = get_best_event(available_events, SLOTS)
        if len(slots) == 0:
            print("Restarting random solution generator...")
            # available_events = EVENTS[:]
            # SLOTS = []
            # continue
            return getRandomSolution()
        available_events.remove(temp)
        # slot = slots[random.randint(0, len(slots)-1)]
        # selects the slot with the biggest number of rooms
        slot_id = slots[0][0]

        SLOTS[slot_id].event_room[temp.id] = slots[0][2][random.randint(
            0, len(slots[0][2])-1)]

    return SLOTS

def getAllNeighbours(solution):
    ret = []
    for i, slot1 in enumerate(solution):
        for event, room in slot1.event_room.items():
            for j, slot2 in enumerate(solution):
                print(i, event, j)
                temp = cp.deepcopy(solution)
                temp[i].event_room.pop(event)
                temp[j].event_room[event] = room
                if isSolutionFeasible(temp):
                    ret.append(temp)

    print(ret)

def getRandomNeighbour(solution):
    neighbours = getAllNeighbours(solution)
    return neighbours[random.randint(0, len(neighbours)-1)]

def isSolutionFeasible(solution):
    eventrooms = []
    for i in range(num_events):
        for slot in solution:
            if i in slot.event_room:
                eventrooms.append(slot.event_room[i])

    eventslots = []
    unplaced = 0
    unsuitablerooms = 0
    for e in range(0, num_events):
        for slot in solution:
            if e in slot.event_room:
                eventslots.append(slot.id)
        if eventrooms[e] == -1 or eventrooms[e] == -1:
            unplaced += 1
        size = 0
        badroom = False
        for g in range(0, num_students):
            if students_events[g][e]:
                size += 1
        if eventrooms[e] != -1 and ROOMS[eventrooms[e]].size < size:
            badroom = True
        for f in range(0, num_features):
            if eventrooms[e] != -1 and events_features[e][f] and not rooms_features[eventrooms[e]][f]:
                badroom = True
        if badroom:
            unsuitablerooms += 1

    studentclashes = 0
    for g in range(0, num_students):
        for e in range(0, num_events):
            for f in range(0, e):
                if eventslots[e] != -1 and eventslots[f] != -1 and students_events[g][e] and students_events[g][f] and eventslots[e] == eventslots[f]:
                    studentclashes += 1

    roomclashes = 0
    for e in range(0, num_events) :
        for f in range(0, e) :
            if eventslots[e] != -1 and eventslots[f]!=-1 and eventrooms[e]!=-1 and eventrooms[f]!=-1 and eventslots[e]==eventslots[f] and eventrooms[e]==eventrooms[f] :
                roomclashes += 1

    return (unplaced+unsuitablerooms+studentclashes+roomclashes) == 0

def value(solution):
    eventslots = []
    for i in range(num_events):
        for slot in solution:
            if i in slot.event_room:
                eventslots.append(slot.id)

    studentavailability = np.full((45, num_students), True)
    for g in range(0, num_students):
        for e in range(0, num_events):
            if students_events[g][e]:
                studentavailability[eventslots[e]][g] = False

    # Count the number of occurrences of a student having more than two classes consecutively (3 consecutively scores 1, 4 consecutively scores 2, 5 consecutively scores 3, etc). Classes at the end of the day followed by classes at the beginning of the next day do not count as consecutive.
    longintensive = 0
    for g in range(0, num_students):
        for d in range(0, 5):
            count = 0
            for t in range(0, 9):
                slot = d*9+t
                if studentavailability[slot][g] == False:
                    count += 1
                else:
                    count = 0
                if count >= 3:
                    longintensive += 1

    # Count the number of occurences of a student having just one class on a day (e.g. count 2 if a student has two days with only one class).
    single = 0
    for g in range(0, num_students):
        for d in range(0, 5):
            count = 0
            badslot = -1
            for t in range(0, 9):
                slot = d*9+t
                if studentavailability[slot][g] == False:
                    count += 1
                    badslot = slot
            if count == 1:
                single += 1

    # Count the number of occurrences of a student having a class in the last timeslot of the day.
    endofday = 0
    for g in range(0, num_students):
        if studentavailability[8][g] == False:
            endofday += 1
        if studentavailability[17][g] == False:
            endofday += 1
        if studentavailability[26][g] == False:
            endofday += 1
        if studentavailability[35][g] == False:
            endofday += 1
        if studentavailability[44][g] == False:
            endofday += 1

    # Sum the three counts to give the solution score - smaller is better - zero is always possible with the instances in this competition.
    return longintensive + single + endofday

def removeEvent(aloc, event):
    for s in aloc:
        if event in s.event_room.keys():
            room = s.event_room[event]
            s.event_room.pop(event)
            return s.id, room

def addEventToSlot(aloc, event, slot, room):
    aloc[slot].event_room[event] = room

def removeEventFromSlot(aloc, event, slot):
    aloc[slot].event_room.pop(event)

def getBestNeighbour(initial):
    initial_copy = cp.deepcopy(initial)
    best_aloc = initial
    best_value = value(initial)

    for e in EVENTS:
        print("Moving event {}".format(e.id))
        e_slot, e_room = removeEvent(initial_copy, e.id)
        e_possible_slots = get_possible_slots(e, initial_copy)
        for i, s in enumerate(e_possible_slots):
            for r in e_possible_slots[i][2]:
                addEventToSlot(initial_copy, e.id, s[0], r)
                new_value = value(initial_copy)
                if new_value < best_value:
                    best_aloc = cp.deepcopy(initial_copy)
                    best_value = new_value
                
                removeEventFromSlot(initial_copy, e.id, s[0])
        
        addEventToSlot(initial_copy, e.id, e_slot, e_room)
    
    return best_aloc, best_value




s = getRandomSolution()
for x in s:
    print(x.id, x.event_room)

s1, v = getBestNeighbour(s)
for x in s:
    print(x.id, x.event_room)
print(v)


# getAllNeighbours(s)
