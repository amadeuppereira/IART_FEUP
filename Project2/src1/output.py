from settings import filename

# For each event, in the order of the problem file, one per line:

# The timeslot number, the room number.
# The timeslot number is an integer between 0 and 44 representing the timeslots allocated to the event.

# The room is the room number assigned to the event. Rooms are numbered in the order from the problem file, starting at zero.


def write_to_file(slots, num_events):
    output_file = open(filename + ".sln", "w")
    for i in range(num_events):
        for slot in slots:
            if i in slot.event_room:
                output_file.write(str(slot.id) + " " +
                                  str(slot.event_room[i]) + "\n")

    output_file.close()
