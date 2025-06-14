def accommodate(*args,**kwargs):
    result = ''
    rooms = dict(sorted(kwargs.items(), key=lambda kv: (kv[1],int((kv[0][-3:]))) ))
    accommodates_rooms = {}
    no_accommodation_guest = 0

    for persons in args:
        found_room = None
        for room, capacity in rooms.items():
            if capacity >= persons:
                accommodates_rooms[room] = persons
                found_room = room
                break
        else:
            no_accommodation_guest += persons

        if found_room:
            del rooms[found_room]

    total_accommodates_rooms = len(accommodates_rooms)
    total_free_roms = len(rooms)

    if total_accommodates_rooms > 0:
        result += f'A total of {total_accommodates_rooms} accommodations were completed!\n'
        for r, g in sorted(accommodates_rooms.items(), key=lambda rg: int(rg[0][-3:])):
            room_number = r[-3:]
            result += f'<Room {room_number} accommodates {g} guests>\n'
    else:
        result += 'No accommodations were completed!\n'

    if no_accommodation_guest > 0:
        result += f'Guests with no accommodation: {no_accommodation_guest}\n'
    if total_free_roms > 0:
        result += f'Empty rooms: {total_free_roms}'

    return result


print(accommodate(10, 9, 8, room_307=6, room_802=5))