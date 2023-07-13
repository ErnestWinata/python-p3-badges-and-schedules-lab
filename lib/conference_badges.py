def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    rooms = range(1, 9)
    assignments = []
    for room in rooms:
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
    return assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
