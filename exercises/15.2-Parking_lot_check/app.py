parking_state = [
[1,1,1],
[0,0,0],
[1,1,2]
]

#Your code go here:
def get_parking_lot(current_park):
    state = {}
    state["occupiedSlots"] = 0
    state["availableSlots"] = 0
    for num in range(0, len(current_park)):
        for i in current_park[num]:
            if i == 1:
                state["occupiedSlots"] = state["occupiedSlots"] + 1
            elif i == 2:
                state["availableSlots"] = state["availableSlots"] + 1
    state["totalSlots"] = state["occupiedSlots"] + state["availableSlots"]
    return state




print(get_parking_lot(parking_state))