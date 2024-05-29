class QAEngineer:
    def verify_room(self, room):
        print(f"Verifying room '{room.name}'...")
        if room.exits:
            print("Exits are present.")
        else:
            print("No exits found.")
        if room.items:
            print("Items are present.")
        else:
            print("No items found.")
