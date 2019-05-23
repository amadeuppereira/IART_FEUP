from settings import TIMESLOTS, SLOTS_PER_DAY
from helper import Helper
from input import EVENTS, ROOMS, STUDENTS, num_features
import copy as cp
import random

helper = Helper()

class Slot:
    def __init__(self, id):
        self.id = id
        self.n_events = 0
        self.distribution = {}

    def update(self, event, room):
        self.distribution[event] = room

    def remove(self, event):
        try:
            self.distribution.pop(event)
        except KeyError:
            pass
        
    def __repr__(self):
        return str(self.id) + " " + str(self.distribution)

class Allocation:
    def __init__(self, nslots):
        self.slots = {}
        for i in range(nslots):
            self.slots[i] = Slot(i)

    def getValuableSlots(self):
        ret = {}
        for i in range(len(self.slots)):
            if(i % (SLOTS_PER_DAY) != 8):
                ret[i] = self.slots[i]
        return ret

    def allocate(self, slot, event, room = None):
        self.slots[slot].update(event, room)

    def updateEventRoom(self, slot, event, room):
        self.slots[slot].update(event, room)

    def removeEvent(self, slot, event):
        self.slots[slot].remove(event)

    def isFeasible(self):
        for _, slot in self.slots.items():
            used_rooms = []
            students = []
            for event, room in slot.distribution.items():
                if room in helper.getEventRooms(event) and room not in used_rooms:
                    used_rooms.append(room)
                else:
                    print(room, slot.id)
                    return False
            
        return True
                




# ----- ----- ----- ----- ----- -----

def getPossibleSlots(event, slots):
    ret = []
    for slot in slots.values():
        flag = True
        events = slot.distribution.keys()
        if len(events) > len(ROOMS):
            continue
        rooms = slot.distribution.values()
        if not all(r in rooms for r in helper.getEventRooms(event.id)):
            for event_id in events:
                if not helper.isCompatible(event.id, event_id):
                    flag = False
                    break

            if flag:
                ret.append(slot.id)

    ret.sort(key=lambda x: slots[x].n_events)
    return ret

def generateRandomAllocation():
    print("Generating Random Allocation")
    alloc = Allocation(TIMESLOTS)
    unassignedEvents = []
    slots = alloc.getValuableSlots()
    
    for e in EVENTS[:]:
        possibleSlots = getPossibleSlots(e, slots)
        if len(possibleSlots) > 0:
            alloc.allocate(possibleSlots[0], e.id)
        else:
            unassignedEvents.append(e.id)

    # update event rooms
    for s in slots.values():
        matches = distributeEventRooms(s)
        events = s.distribution.copy().keys()
        for e in events:
            try:
                room = matches.index(e)
                alloc.updateEventRoom(s.id, e, room)
            except ValueError:
                unassignedEvents.append(e)
                alloc.removeEvent(s.id, e)

    for e in unassignedEvents.copy():
        if tryPlaceEvent(e, slots):
            unassignedEvents.remove(e)

    shuffleSlots(slots, unassignedEvents)

    best = slots, unassignedEvents
    for i in range(100):
        print("Blowing up {}/{} ({} unassigned events)".format(i, 100, len(best[1])))
        temp_best = best
        for _ in range(5):
            slotsCopy = cp.deepcopy(best[0])
            uaCopy = best[1].copy()
            blowupSlots(slotsCopy, uaCopy)
            if len(uaCopy) < len(best[1]):
                temp_best = slotsCopy, uaCopy

        best = temp_best
        if len(best[1]) == 0:
            print("Finished blowing up!")
            break

    unassignedEvents = best[1]
    slots = best[0]

    if len(unassignedEvents) > 0:
        print("Opening end of the day slots")
        for e in unassignedEvents.copy():
            if tryPlaceEvent(e, alloc.slots):
                unassignedEvents.remove(e)

    if len(unassignedEvents) > 0:
        print("Couldn't find feasible allocation! Retrying...")
        return generateRandomAllocation()
    else:
        print("Allocation found!")

    return alloc

def blowupSlots(slots, unassignedEvents):
    e = random.choice(unassignedEvents)
    _, s = random.choice(list(slots.items()))
    temp = cp.deepcopy(s)
    prevEvents = temp.distribution.keys()
    temp.distribution = {e: None}
    unassignedEvents.remove(e)
    for prevE in prevEvents:
        if helper.isCompatible(prevE, e):
            temp.update(prevE, None)
        else:
            unassignedEvents.append(prevE)

    matches = distributeEventRooms(temp)
    for e1 in temp.distribution.keys():
        try:
            room = matches.index(e1)
            s.update(e1, room)
        except ValueError:
            unassignedEvents.append(e1)
            s.remove(e1)

    for e in unassignedEvents.copy():
        if tryPlaceEvent(e, slots):
            unassignedEvents.remove(e)

    shuffleSlots(slots, unassignedEvents, 5000)

def shuffleSlots(slots, unassignedEvents, n = 50000):
    for _ in range(n):
        for e in unassignedEvents.copy():
            _, s = random.choice(list(slots.items()))
            if all(helper.isCompatible(e, e1) for e1 in s.distribution.keys()):
                temp = cp.deepcopy(s)
                temp.update(e, None)
                unassignedEvents.remove(e)
                matches = distributeEventRooms(temp, True)
                n_allocated = sum(1 for m in matches if m is not None)
                if n_allocated > len(s.distribution):
                    for e1 in temp.distribution.keys():
                        s.update(e1, matches.index(e1))

                elif n_allocated == len(s.distribution):
                    # for ex in s.distribution.keys():
                    #     unassignedEvents.append(ex)
                    # s.distribution = {}
                    unplaced = []
                    for e1 in temp.distribution.keys():
                        try:
                            room = matches.index(e1)
                            s.update(e1, room)
                            # unassignedEvents.remove(e1)
                        except ValueError:
                            unplaced.append(e1)
                            s.remove(e1)
                    for e1 in unplaced:
                        if not tryPlaceEvent(e1, slots):
                                unassignedEvents.append(e1)

def tryPlaceEvent(eventid, slots):
    for s in slots.values():
        if len(s.distribution) >= len(ROOMS):
            continue
        if all(helper.isCompatible(eventid, e1) for e1 in s.distribution.keys()):
            temp = cp.deepcopy(s)
            temp.update(eventid, None)
            matches = distributeEventRooms(temp)
            if sum(1 for m in matches if m is not None) == len(temp.distribution):
                for e1 in temp.distribution.keys():
                    s.update(e1, matches.index(e1))
                return True
    return False

def distributeEventRooms(slot, randomize = False):
    matches = [None] * len(ROOMS)
    temp = list(slot.distribution.keys()).copy()
    if randomize:
        random.shuffle(temp)
    for id in temp:
        seen = [False] * len(ROOMS) 
        distributeEventRoomsHelper(id, matches, seen)

    return matches

def distributeEventRoomsHelper(id, matches, seen):
    for r in range(len(ROOMS)): 
        if r in helper.getEventRooms(id) and seen[r] == False: 
            seen[r] = True 
            if not matches[r] or distributeEventRoomsHelper(matches[r], matches, seen): 
                matches[r] = id 
                return True
    return False



alloc = generateRandomAllocation()
print(alloc.isFeasible())
print(alloc.slots)



# eventrooms = []
#         for i in range(len(EVENTS)):
#             for _, slot in self.slots.items():
#                 if i in slot.distribution:
#                     eventrooms.append(slot.distribution[i])
#                     break

#         eventslots = []
#         unplaced = 0
#         unsuitablerooms = 0
#         for e in EVENTS:
#             for _, slot in self.slots.items():
#                 if e.id in slot.distribution:
#                     eventslots.append(slot.id)
#             if eventrooms[e.id] == None:
#                 print("eventrooms[e.id] == None")
#                 print(e.id)
#                 return False
#             size = 0
#             badroom = False
#             for s in STUDENTS:
#                 if e.id in s.events:
#                     size += 1
#             if eventrooms[e.id] != None and ROOMS[eventrooms[e.id]].size < size:
#                 badroom = True
#             for f in range(num_features):
#                 if eventrooms[e.id] != None and f in e.features and not f in ROOMS[eventrooms[e.id]].features:
#                     badroom = True
#             if badroom:
#                 print("badroom")
#                 return False

#         studentclashes = 0
#         for g in range(len(STUDENTS)):
#             for e in range(len(EVENTS)):
#                 for f in range(e):
#                     if eventslots[e] != None and eventslots[f] != None and e in STUDENTS[g].events and f in STUDENTS[g].events and eventslots[e] == eventslots[f]:
#                         print("if eventslots[e] != -1 and eventslots[f] != -1 and e in STUDENTS[g].events and f in STUDENTS[g].events and eventslots[e] == eventslots[f]:")
#                         return False

#         roomclashes = 0
#         for e in range(len(EVENTS)):
#             for f in range(e):
#                 if eventslots[e] != None and eventslots[f] != None and eventrooms[e] != None and eventrooms[f] != None and eventslots[e] == eventslots[f] and eventrooms[e] == eventrooms[f]:
#                     print("if eventslots[e] != -1 and eventslots[f] != -1 and eventrooms[e] != -1 and eventrooms[f] != -1 and eventslots[e] == eventslots[f] and eventrooms[e] == eventrooms[f]:")
#                     return False

#         return True