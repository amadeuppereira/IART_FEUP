from settings import *

output_file = open(filename + ".sln", "w")


# For each event, in the order of the problem file, one per line:

# The timeslot number, the room number.
# The timeslot number is an integer between 0 and 44 representing the timeslots allocated to the event.

# The room is the room number assigned to the event. Rooms are numbered in the order from the problem file, starting at zero.

# Write to file here
output_file.write("1 1 2 2 2 2 1 1")



output_file.close()