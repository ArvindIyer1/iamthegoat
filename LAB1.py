status = {
    "A" : "Dirty",
    "B": "Dirty"
}

def vacuum(loc_room,status):
    if(status[loc_room] == "Dirty"):
        print(f"Action suck at {loc_room}")
        status[loc_room] = "Clean"
    else:
        if(loc_room == "A"):
            print("Room A is Clean")
            print(f"Move left to room B")
            loc_room = "B"
            print(f"Action suck at {loc_room}")
        else:
            print("Now room B is cleaned")
            status[loc_room] = "Clean"
            loc_room = "A"
    
    return loc_room,status

loc_room = "A"


while True:
    loc_room,status = vacuum(loc_room,status)

    if(status["A"] == "Clean" and status["B"] == "Clean"):
        print("Both the rooms are clean")
        break