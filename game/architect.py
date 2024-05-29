class Architect:
    def add_room(self, game, room_name, room_description, items=None, exits=None):
        new_room = Room(room_name, room_description, items)
        game.rooms[room_name] = new_room
        if exits:
            new_room.exits = exits
        print(f"Room '{room_name}' added to the game.")
