import numpy as np
from settings import *
from input import *
from output import *
import random
import copy as cp
import time


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


def get_possible_slots(event, slots):
    # each elements is [slot id, current number os events, [available rooms id]]
    ret = []
    for slot in slots:
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
            return False
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
            return False

    studentclashes = 0
    for g in range(0, num_students):
        for e in range(0, num_events):
            for f in range(0, e):
                if eventslots[e] != -1 and eventslots[f] != -1 and students_events[g][e] and students_events[g][f] and eventslots[e] == eventslots[f]:
                    return False

    roomclashes = 0
    for e in range(0, num_events):
        for f in range(0, e):
            if eventslots[e] != -1 and eventslots[f] != -1 and eventrooms[e] != -1 and eventrooms[f] != -1 and eventslots[e] == eventslots[f] and eventrooms[e] == eventrooms[f]:
                return False

    return True


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

    longintensive = 0
    single = 0
    endofday = 0
    for g in range(0, num_students):
        for d in range(0, 5):
            countA = 0
            countB = 0
            badslot = -1
            for t in range(0, 9):
                slot = d*9+t
                if studentavailability[slot][g] == False:
                    countA += 1
                    countB += 1
                    badslot = slot
                else:
                    countA = 0
                if countA >= 3:
                    longintensive += 1
            if countB == 1:
                single += 1

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

    return longintensive + single + endofday


def removeEvent(aloc, event):
    for s in aloc:
        if event in s.event_room.keys():
            room = s.event_room.pop(event)
            return s.id, room


def addEventToSlot(aloc, event, slot, room):
    aloc[slot].event_room[event] = room


def removeEventFromSlot(aloc, event, slot):
    aloc[slot].event_room.pop(event)


# def getBestNeighbour(initial):
#     initial_copy = cp.deepcopy(initial)
#     best_aloc = initial
#     best_value = value(initial)

#     for e in EVENTS:
#         print("Moving event {}".format(e.id))
#         e_slot, e_room = removeEvent(initial_copy, e.id)
#         e_possible_slots = get_possible_slots(e, initial_copy)
#         for i, s in enumerate(e_possible_slots):
#             for r in e_possible_slots[i][2]:
#                 addEventToSlot(initial_copy, e.id, s[0], r)
#                 new_value = value(initial_copy)
#                 if new_value < best_value:
#                     best_aloc = cp.deepcopy(initial_copy)
#                     best_value = new_value

#                 removeEventFromSlot(initial_copy, e.id, s[0])

#         addEventToSlot(initial_copy, e.id, e_slot, e_room)

#     return best_aloc, best_value

def getBestNeighbour(initial):
    initial_copy = cp.deepcopy(initial)
    best_value = value(initial)

    best = []

    for e in EVENTS:
        print("Moving event {}".format(e.id))
        e_slot, e_room = removeEvent(initial_copy, e.id)
        e_possible_slots = get_possible_slots(e, initial_copy)
        for i, s in enumerate(e_possible_slots):
            for r in e_possible_slots[i][2]:
                addEventToSlot(initial_copy, e.id, s[0], r)
                new_value = value(initial_copy)
                if new_value < best_value:
                    best_value = new_value
                    best.append([cp.deepcopy(initial_copy), new_value])
                elif new_value == best_value:
                    best.append([cp.deepcopy(initial_copy), new_value])

                removeEventFromSlot(initial_copy, e.id, s[0])

        addEventToSlot(initial_copy, e.id, e_slot, e_room)

    if initial in best:
        best.pop(initial)

    best_list = [k for k, v in best if v == best_value]
    if len(best_list) == 0:
        return initial, best_value

    best_aloc = best_list[random.randint(0, len(best_list)-1)]

    return best_aloc, best_value


# Returns a random neighbour
def getRandomNeighbour(initial):
    initial_copy = cp.deepcopy(initial)
    event_id = random.randint(0, num_events-1)
    event = EVENTS[event_id]
    slot_id, slot_room = removeEvent(initial_copy, event_id)

    possible_slots = get_possible_slots(event, initial_copy)
    if len(possible_slots) == 0:
        getRandomNeighbour(initial)
    slot = possible_slots[random.randint(0, len(possible_slots)-1)]
    if len(slot[2]) == 0:
        getRandomNeighbour(initial)
    room = slot[2][random.randint(0, len(slot[2])-1)]

    addEventToSlot(initial_copy, event_id, slot[0], room)
    return initial_copy


# Returns a random neighbour that has a better value than initial_value
def getBetterRandomNeighbour(initial, initial_value, max_attemps):
    if max_attemps == 0:
        return initial, initial_value

    new_attemps = max_attemps - 1

    initial_copy = cp.deepcopy(initial)
    event_id = random.randint(0, num_events-1)
    event = EVENTS[event_id]
    slot_id, slot_room = removeEvent(initial_copy, event_id)

    possible_slots = get_possible_slots(event, initial_copy)
    if len(possible_slots) == 0:

        return getBetterRandomNeighbour(initial, initial_value, new_attemps)
    slot = possible_slots[random.randint(0, len(possible_slots)-1)]
    if len(slot[2]) == 0:
        return getBetterRandomNeighbour(initial, initial_value, new_attemps)
    room = slot[2][random.randint(0, len(slot[2])-1)]

    addEventToSlot(initial_copy, event_id, slot[0], room)

    copy_value = value(initial_copy)
    if copy_value >= initial_value:
        return getBetterRandomNeighbour(initial, initial_value, new_attemps)

    return initial_copy, copy_value


# s = getRandomSolution()
# print(value(s))
# random, random_value = getRandomNeighbour(s, value(s))
# print(random_value)


# getBestNeighbour2(s)

# print(isSolutionFeasible(s))

# for x in s:
#     print(x.id, x.event_room)
# print(value(s))

# s1, v = getBestNeighbour(s)
# for x in s:
#     print(x.id, x.event_room)
# print(v)

# getAllNeighbours(s)
