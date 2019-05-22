from settings import TIMESLOTS, SLOTS_PER_DAY
from helper import Helper
from input import EVENTS, ROOMS

helper = Helper()

class Slot:
    def __init__(self, id):
        self.id = id
        self.n_events = 0
        self.distribution = {}

    def addEvent(self, event, room):
        self.distribution[event] = room
        
    def __repr__(self):
        return str(self.id) + " " + str(self.distribution)

class Alocation:
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

    def alocate(self, slot, event, room = None):
        self.slots[slot].addEvent(event, room)


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

def generateRandomAlocation():
    aloc = Alocation(TIMESLOTS)
    unasignedEvents = []
    slots = aloc.getValuableSlots()
    for e in EVENTS[:]:
        possibleSlots = getPossibleSlots(e, slots)
        if len(possibleSlots) > 0:
            aloc.alocate(possibleSlots[0], e.id)
        else:
            unasignedEvents.append(e)

    distributeEventRooms()

# fix
def distributeEventRooms():
    matches = [None] * len(ROOMS)
    for id in range(len(EVENTS)):
        seen = [False] * len(ROOMS) 
        distributeEventRoomsHelper(id, matches, seen)
    
    print(matches)

def distributeEventRoomsHelper(id, matches, seen):
    for r in range(len(ROOMS)): 
        if r in helper.getEventRooms(id) and seen[r] == False: 
            seen[r] = True 
            if not matches[r] or distributeEventRoomsHelper(matches[r], matches, seen): 
                matches[r] = id 
                return

# class GFG: 
#     def __init__(self, graph): 
#         self.graph = graph  
#         self.ppl = len(graph) 
#         self.jobs = len(graph[0]) 
  
#     # A DFS based recursive function 
#     # that returns true if a matching  
#     # for vertex u is possible 
#     def bpm(self, u, matchR, seen): 
  
#         # Try every job one by one 
#         for v in range(self.jobs): 
  
#             # If applicant u is interested  
#             # in job v and v is not seen 
#             if self.graph[u][v] and seen[v] == False: 
                  
#                 # Mark v as visited 
#                 seen[v] = True 
  
#                 '''If job 'v' is not assigned to 
#                    an applicant OR previously assigned  
#                    applicant for job v (which is matchR[v])  
#                    has an alternate job available.  
#                    Since v is marked as visited in the  
#                    above line, matchR[v]  in the following 
#                    recursive call will not get job 'v' again'''
#                 if matchR[v] == -1 or self.bpm(matchR[v],  
#                                                matchR, seen): 
#                     matchR[v] = u 
#                     return True
#         return False
  
#     # Returns maximum number of matching  
#     def maxBPM(self): 
#         '''An array to keep track of the  
#            applicants assigned to jobs.  
#            The value of matchR[i] is the  
#            applicant number assigned to job i,  
#            the value -1 indicates nobody is assigned.'''
#         matchR = [-1] * self.jobs 
          
#         # Count of jobs assigned to applicants 
#         result = 0 
#         for i in range(self.ppl): 
              
#             # Mark all jobs as not seen for next applicant. 
#             seen = [False] * self.jobs 
              
#             # Find if the applicant 'u' can get a job 
#             if self.bpm(i, matchR, seen): 
#                 result += 1
#         return result

generateRandomAlocation()



