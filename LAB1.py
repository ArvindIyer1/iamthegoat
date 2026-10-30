state = {"A": "Dirty", "B": "Dirty"}


def act(room):
    if state[room] == "Dirty":
        print(f"Suck dirt in room {room}")
        state[room] = "Clean"
    else:
        print(f"Room {room} is clean")
        room = "B" if room == "A" else "A"
        print(f"Move to room {room}")
    return room


room = "A"

while "Dirty" in state.values():
    room = act(room)

print("Both rooms are clean")
