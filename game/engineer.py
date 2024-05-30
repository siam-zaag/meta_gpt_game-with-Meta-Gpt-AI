class Engineer:
    def create_item(self, room, item):
        print('-----room',room)
        room.items.append(item)
        print(f"Item '{item}' added to {room.name}.")
