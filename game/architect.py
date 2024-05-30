from rooms import Room

class Architect:
    def add_room(self, game, room_name, room_description, items=None, exits=None):
        _room_name = room_name.title()
        new_room = Room(_room_name, room_description, items)
        game.rooms[_room_name] = new_room
        if exits:
            new_room.exits = exits
        print(f"Room '{_room_name}' added to the game.")
