
status = {
    "A": "Dirty",
    "B": "Dirty"
}

def vacuum(loc_room, status):
    if status[loc_room] == "Dirty":
        print("Action: Suck at", loc_room)
        status[loc_room] = "Clean"

    else:
        if loc_room == "A":
            print("Room A is Clean")
            print("Move right to room B")
            loc_room = "B"
        else:
            print("Room B is Clean")
            print("Move left to room A")
            loc_room = "A"

    return loc_room, status

loc_room = "A"

while True:
    loc_room, status = vacuum(loc_room, status)

    if status["A"] == "Clean" and status["B"] == "Clean":
        print("Both rooms are clean")
        break
