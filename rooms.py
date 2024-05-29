class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.exits = {}

    def describe(self):
        print(f"{self.name}\n{self.description}")
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item}")
        if self.exits:
            print("Exits:")
            for direction in self.exits:
                print(f"- {direction}")
