from input import ROOMS, STUDENTS, EVENTS

class Helper:
    def __init__(self):
        self.handleEventStudents()
        self.handleEventRooms()
        self.handleIncidence()

    def handleEventStudents(self):
        self.event_students = []
        for e in EVENTS:
            self.event_students.append([])
            for s in STUDENTS:
                if e.id in s.events:
                    self.event_students[e.id].append(s.id)

    def handleEventRooms(self):
        self.event_rooms = []
        for e in EVENTS:
            self.event_rooms.append([])
            for r in ROOMS:
                if (r.size >= len(self.event_students[e.id])) and (set(e.features).issubset(set(r.features))):
                    self.event_rooms[e.id].append(r.id)
        
    def handleIncidence(self):
        self.incidence = [[False for x in range(len(EVENTS))] for y in range(len(EVENTS))]
        for e1 in EVENTS:
            for e2 in EVENTS:
                if not any(s in self.event_students[e2.id] for s in self.event_students[e1.id]):
                    self.incidence[e1.id][e2.id] = True

        for e1 in EVENTS:
            if len(self.event_rooms[e1.id]) == 1:
                for e2 in EVENTS:
                    if len(self.event_rooms[e2.id]) == 1 and self.event_rooms[e1.id][0] == self.event_rooms[e2.id][0]:
                        self.incidence[e1.id][e2.id] = False

    def getEventRooms(self, id):
        return self.event_rooms[id]

    def isCompatible(self, id1, id2):
        return self.incidence[id1][id2]