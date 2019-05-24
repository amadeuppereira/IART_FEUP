from settings import TIMESLOTS, SLOTS_PER_DAY, FILENAME
from helper import Helper
from input import EVENTS, ROOMS, STUDENTS, num_features
import copy as cp
import numpy as np
import random

helper = Helper()


class Slot:
    def __init__(self, id):
        self.id = id
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
        self.alloc_value = None
        self.event_data = {}
        for i in range(nslots):
            self.slots[i] = Slot(i)

    def getValuableSlots(self):
        ret = {}
        for i in range(len(self.slots)):
            if(i % SLOTS_PER_DAY != SLOTS_PER_DAY - 1):
                ret[i] = self.slots[i]
        return ret

    def finish(self):
        for slotid, slot in self.slots.items():
            for eventid, room in slot.distribution.items():
                self.event_data[eventid] = (slotid, room)

    def allocate(self, slot, event, room=None):
        self.alloc_value = None
        self.slots[slot].update(event, room)
        self.event_data[event] = (slot, room)

    def updateEventRoom(self, slot, event, room):
        self.alloc_value = None
        self.slots[slot].update(event, room)
        self.event_data[event] = (slot, room)

    def removeEvent(self, slot, event):
        self.alloc_value = None
        self.slots[slot].remove(event)
        self.event_data.pop(event)

    def removeEvent1(self, event):
        self.alloc_value = None
        s, r = self.event_data.pop(event)
        self.slots[s].remove(event)
        return s, r

    def isFeasible(self):
        used_events = set()
        for _, slot in self.slots.items():
            used_rooms = []
            students = []
            for event, room in slot.distribution.items():
                if room in helper.getEventRooms(event) and room not in used_rooms:
                    used_rooms.append(room)
                else:
                    return False

                for s in helper.getEventStudents(event):
                    if s in students:
                        return False
                    students.append(s)

                used_events.add(event)

        return len(used_events) == len(EVENTS)

    def value(self):
        if self.alloc_value:
            return self.alloc_value

        single_event = 0
        end_of_day = 0
        intensive = 0

        if not self.event_data:
            self.finish()

        slot_counter = 0
        for _ in range(int(TIMESLOTS / SLOTS_PER_DAY)):
            students = []
            for _ in range(SLOTS_PER_DAY):
                slot = self.slots[slot_counter]
                slot_counter += 1
                for eventid, _ in slot.distribution.items():
                    n_students = helper.getEventStudents(eventid)
                    if slot.id % SLOTS_PER_DAY == SLOTS_PER_DAY - 1:
                        end_of_day += len(n_students)
                    students += n_students
            single_event += len(list(filter(lambda x: students.count(x) == 1, students)))

        for s in STUDENTS:
            student_slots = []
            for eventid in s.events:
                try:
                    student_slots.append(self.event_data[eventid][0])
                except KeyError:
                    pass

            new_student_slots = []
            for i in range(int(TIMESLOTS / SLOTS_PER_DAY)):
                new_student_slots.append([])

            for temp in student_slots:
                idx = temp // SLOTS_PER_DAY
                new_student_slots[idx].append(temp)

            for temp in new_student_slots:
                temp.sort()

            consecutives = []

            for temp in new_student_slots:
                if not temp:
                    continue
                previous = temp[0]
                counter = 1
                consecutives.append(counter)
                for temp1 in temp[:]:
                    if temp1 == previous + 1:
                        consecutives.pop()
                        counter += 1
                        consecutives.append(counter)
                    else:
                        counter = 1
                        consecutives.append(counter)
                    previous = temp1

            intensive += sum(list(map(lambda x: x-2 if x -
                                      2 > 0 else 0, consecutives)))

        value = single_event + end_of_day + intensive
        if not self.isFeasible():
            value += 10000
        self.alloc_value = value
        return value

    def writeToFile(self):
        output_file = open(FILENAME + ".sln", "w")
        for i in range(len(EVENTS)):
            for slot in self.slots.values():
                if i in slot.distribution.keys():
                    output_file.write(str(slot.id) + " " +
                                      str(slot.distribution[i]) + "\n")
                    break

        output_file.close()

    def getBestNeighbour(self):
        initial_copy = self.copy()
        best_alloc = None
        best_value = float('Inf')

        for e in EVENTS:
            # print("Moving event {}".format(e.id))
            e_slot, e_room = initial_copy.removeEvent1(e.id)

            # MOVES
            e_possible_slots = getPossibleSlots(e, initial_copy.slots)
            for i, s in enumerate(e_possible_slots):
                for r in e_possible_slots[i][1]:
                    initial_copy.allocate(s[0], e.id, r)
                    new_value = initial_copy.value()
                    if new_value < best_value:
                        best_alloc = cp.deepcopy(initial_copy)
                        best_value = new_value

                    initial_copy.removeEvent1(e.id)

            # SWAPS
            for e1 in EVENTS:
                if e1.id == e.id:
                    continue
                e1_slot, e1_room = initial_copy.removeEvent1(e1.id)
                if all(helper.isCompatible(e.id, eTemp) for eTemp in initial_copy.slots[e1_slot].distribution.keys()) and \
                        all(helper.isCompatible(e1.id, eTemp) for eTemp in initial_copy.slots[e_slot].distribution.keys()):
                    usable_rooms_e = np.setdiff1d(helper.getEventRooms(
                        e.id), initial_copy.slots[e1_slot].distribution.keys())
                    if len(usable_rooms_e) > 0:
                        usable_rooms_e1 = np.setdiff1d(helper.getEventRooms(
                            e1.id), initial_copy.slots[e_slot].distribution.keys())
                        if len(usable_rooms_e1) > 0:
                            for r in usable_rooms_e:
                                initial_copy.allocate(e1_slot, e.id, r)
                                for r1 in usable_rooms_e1:
                                    initial_copy.allocate(e_slot, e1.id, r1)
                                    new_value = initial_copy.value()
                                    if new_value < best_value:
                                        best_alloc = cp.deepcopy(initial_copy)
                                        best_value = new_value
                                    initial_copy.removeEvent(e_slot, e1.id)

                                initial_copy.removeEvent(e1_slot, e.id)
                initial_copy.allocate(e1_slot, e1.id, e1_room)

            initial_copy.allocate(e_slot, e.id, e_room)

        return best_alloc, best_value


# ----- ----- ----- ----- ----- -----

def getBestNeighbour(allocation):
    initial_copy = cp.deepcopy(allocation)
    best_alloc = None
    best_value = float('Inf')

    for e in EVENTS:
        # print("Moving event {}".format(e.id), end='\r')
        e_slot, e_room = initial_copy.removeEvent1(e.id)

        # MOVES
        e_possible_slots = getPossibleSlots(e, initial_copy.slots)
        for i, s in enumerate(e_possible_slots):
            for r in e_possible_slots[i][1]:
                initial_copy.allocate(s[0], e.id, r)
                new_value = initial_copy.value()
                if new_value < best_value:
                    best_alloc = cp.deepcopy(initial_copy)
                    best_value = new_value

                initial_copy.removeEvent1(e.id)

        # SWAPS
        for e1 in EVENTS:
            if e1.id == e.id:
                continue
            e1_slot, e1_room = initial_copy.removeEvent1(e1.id)
            if all(helper.isCompatible(e.id, eTemp) for eTemp in initial_copy.slots[e1_slot].distribution.keys()) and \
                    all(helper.isCompatible(e1.id, eTemp) for eTemp in initial_copy.slots[e_slot].distribution.keys()):
                usable_rooms_e = np.setdiff1d(helper.getEventRooms(
                    e.id), initial_copy.slots[e1_slot].distribution.keys())
                if len(usable_rooms_e) > 0:
                    usable_rooms_e1 = np.setdiff1d(helper.getEventRooms(
                        e1.id), initial_copy.slots[e_slot].distribution.keys())
                    if len(usable_rooms_e1) > 0:
                        for r in usable_rooms_e:
                            initial_copy.allocate(e1_slot, e.id, r)
                            for r1 in usable_rooms_e1:
                                initial_copy.allocate(e_slot, e1.id, r1)
                                new_value = initial_copy.value()
                                if new_value < best_value:
                                    best_alloc = cp.deepcopy(initial_copy)
                                    best_value = new_value
                                initial_copy.removeEvent(e_slot, e1.id)

                            initial_copy.removeEvent(e1_slot, e.id)
            initial_copy.allocate(e1_slot, e1.id, e1_room)

        initial_copy.allocate(e_slot, e.id, e_room)

    return best_alloc, best_value


def getBetterNeighbour(allocation):
    initial_copy = cp.deepcopy(allocation)
    best_alloc = initial_copy
    best_value = initial_copy.value()

    for e in EVENTS:
        e_slot, e_room = initial_copy.removeEvent1(e.id)

        # MOVES
        if random.randint(0, 1):
            e_possible_slots = getPossibleSlots(e, initial_copy.slots)
            for i, s in enumerate(e_possible_slots):
                for r in e_possible_slots[i][1]:
                    initial_copy.allocate(s[0], e.id, r)
                    new_value = initial_copy.value()
                    if new_value < best_value:
                        return initial_copy, new_value

                    initial_copy.removeEvent1(e.id)

        # SWAPS
        else:
            for e1 in EVENTS:
                if e1.id == e.id:
                    continue
                e1_slot, e1_room = initial_copy.removeEvent1(e1.id)
                if all(helper.isCompatible(e.id, eTemp) for eTemp in initial_copy.slots[e1_slot].distribution.keys()) and \
                        all(helper.isCompatible(e1.id, eTemp) for eTemp in initial_copy.slots[e_slot].distribution.keys()):
                    usable_rooms_e = np.setdiff1d(helper.getEventRooms(
                        e.id), initial_copy.slots[e1_slot].distribution.keys())
                    if len(usable_rooms_e) > 0:
                        usable_rooms_e1 = np.setdiff1d(helper.getEventRooms(
                            e1.id), initial_copy.slots[e_slot].distribution.keys())
                        if len(usable_rooms_e1) > 0:
                            for r in usable_rooms_e:
                                initial_copy.allocate(e1_slot, e.id, r)
                                for r1 in usable_rooms_e1:
                                    initial_copy.allocate(e_slot, e1.id, r1)
                                    new_value = initial_copy.value()
                                    if new_value < best_value:
                                        return initial_copy, new_value

                                    initial_copy.removeEvent(e_slot, e1.id)

                                initial_copy.removeEvent(e1_slot, e.id)
                initial_copy.allocate(e1_slot, e1.id, e1_room)

        initial_copy.allocate(e_slot, e.id, e_room)

    return best_alloc, best_value


def getRandomNeighbour(allocation):
    initial_copy = cp.deepcopy(allocation)
    event_id = random.randint(0, len(EVENTS)-1)
    event = EVENTS[event_id]
    slot_id, slot_room = initial_copy.removeEvent1(event_id)

    # MOVE
    # if random.randint(0, 1):
    if False:
        possible_slots = getPossibleSlots(event, initial_copy.slots)
        if len(possible_slots) == 0:
            return getRandomNeighbour(allocation)
        slot = possible_slots[random.randint(0, len(possible_slots)-1)]
        if len(slot[1]) == 0:
            return getRandomNeighbour(allocation)
        room = slot[1][random.randint(0, len(slot[1])-1)]

        initial_copy.allocate(slot[0], event_id, room)
    # SWAP
    else:
        event1_id = random.randint(0, len(EVENTS)-1)
        if event_id == event1_id:
            return getRandomNeighbour(allocation)
        event1 = EVENTS[event1_id]
        e1_slot, e1_room = initial_copy.removeEvent1(event1_id)
        if all(helper.isCompatible(event_id, eTemp) for eTemp in initial_copy.slots[e1_slot].distribution.keys()) and \
                all(helper.isCompatible(event1_id, eTemp) for eTemp in initial_copy.slots[slot_id].distribution.keys()):
            usable_rooms_e = np.setdiff1d(helper.getEventRooms(
                event_id), initial_copy.slots[e1_slot].distribution.keys())
            if len(usable_rooms_e) > 0:
                usable_rooms_e1 = np.setdiff1d(helper.getEventRooms(
                    event1_id), initial_copy.slots[slot_id].distribution.keys())
                if len(usable_rooms_e1) <= 0:
                    return getRandomNeighbour(allocation)
                initial_copy.allocate(
                    e1_slot, event_id, random.choice(usable_rooms_e))
                initial_copy.allocate(slot_id, event1_id,
                                      random.choice(usable_rooms_e1))
            else:
                return getRandomNeighbour(allocation)
        else:
            return getRandomNeighbour(allocation)

    return initial_copy, initial_copy.value()


def getPossibleSlots(event, slots):
    ret = []
    for slot in slots.values():
        flag = True
        events = slot.distribution.keys()
        if len(events) >= len(ROOMS):
            continue
        rooms = slot.distribution.values()
        usable_rooms = np.setdiff1d(helper.getEventRooms(event.id), rooms)
        if len(usable_rooms) > 0:
            for event_id in events:
                if not helper.isCompatible(event.id, event_id):
                    flag = False
                    break

            if flag:
                ret.append((slot.id, usable_rooms))

    ret.sort(key=lambda x: len(slots[x[0]].distribution))
    return ret


def generateRandomAllocation():
    print("Generating Random Allocation")
    alloc = Allocation(TIMESLOTS)
    unassignedEvents = []
    slots = alloc.getValuableSlots()

    for e in EVENTS:
        possibleSlots = getPossibleSlots(e, slots)
        if len(possibleSlots) > 0:
            alloc.allocate(possibleSlots[0][0], e.id)
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
    for i in range(101):
        print("{}/{} ({} unassigned events)".format(i, 100, len(best[1])), end='\r')
        temp_best = best
        for _ in range(3):
            slotsCopy = cp.deepcopy(temp_best[0])
            uaCopy = temp_best[1].copy()
            blowupSlots(slotsCopy, uaCopy)
            if len(uaCopy) < len(temp_best[1]):
                temp_best = (slotsCopy, uaCopy)

        best = temp_best
        if len(best[1]) == 0:
            print("Finished blowing up!")
            break

    slots = best[0]
    unassignedEvents = best[1]

    for i, s in slots.items():
        alloc.slots[i] = s

    if len(unassignedEvents) > 0:
        print("\nOpening end of the day slots")
        for e in unassignedEvents.copy():
            if tryPlaceEvent(e, alloc.slots):
                unassignedEvents.remove(e)

    if len(unassignedEvents) > 0 or not alloc.isFeasible():
        print("Couldn't find feasible allocation! Retrying...")
        return generateRandomAllocation()
    else:
        print("Allocation found!")

    alloc.finish()
    return alloc


def blowupSlots(slots, unassignedEvents):
    if len(unassignedEvents) == 0:
        return

    e = random.choice(unassignedEvents)
    _, s = random.choice(list(slots.items()))

    temp = cp.deepcopy(s)
    prevEvents = list(s.distribution.keys()).copy()
    temp.distribution = {e: None}

    for e1 in prevEvents:
        unassignedEvents.append(e1)
    for prevE in prevEvents:
        if helper.isCompatible(prevE, e):
            temp.update(prevE, None)

    matches = distributeEventRooms(temp)
    s.distribution = {}

    for e1 in temp.distribution.keys():
        try:
            room = matches.index(e1)
            s.update(e1, room)
            unassignedEvents.remove(e1)
        except ValueError:
            pass

    for e1 in unassignedEvents.copy():
        if tryPlaceEvent(e, slots):
            unassignedEvents.remove(e1)

    shuffleSlots(slots, unassignedEvents, 5000)


def shuffleSlots(slots, unassignedEvents, n=50000):
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
                    unplaced = []
                    for e1 in temp.distribution.keys():
                        try:
                            room = matches.index(e1)
                            s.update(e1, room)
                        except ValueError:
                            unplaced.append(e1)
                            s.remove(e1)
                    for e1 in unplaced:
                        if not tryPlaceEvent(e1, slots):
                            unassignedEvents.append(e1)

                else:
                    unassignedEvents.append(e)


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


def distributeEventRooms(slot, randomize=False):
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
