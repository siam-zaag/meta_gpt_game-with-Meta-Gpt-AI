from rooms import Room

class Game:
    def __init__(self):
        self.rooms = {
            'Living Room': Room('Living Room', 'A cozy living room with a fireplace.', ['key', 'map']),
            'Kitchen': Room('Kitchen', 'A kitchen with a strange smell.', ['knife', 'apple']),
            'Bedroom': Room('Bedroom', 'A peaceful bedroom with a comfortable bed.', ['pillow', 'book']),
            'Office room': Room('Office room', 'A peaceful Office room with a comfortable table.', ['laptop', 'PC'])
        }
        self.current_room = self.rooms['Living Room']
        
        # Setting up exits
        self.rooms['Living Room'].exits = {'north': self.rooms['Kitchen'], 
        'east': self.rooms['Bedroom'], 
        'right':self.rooms['Office room']}
        self.rooms['Kitchen'].exits = {'south': self.rooms['Living Room']}
        self.rooms['Bedroom'].exits = {'west': self.rooms['Living Room']}

    def start(self):
        print("Welcome to the Adventure Game!")
        self.current_room.describe()
        while True:
            command = input("> ").strip().lower()
            if command in ['quit', 'exit']:
                print("Thanks for playing!")
                break
            elif command == 'look':
                self.current_room.describe()
            elif command.startswith('go '):
                direction = command.split()[1]
                if direction in self.current_room.exits:
                    self.current_room = self.current_room.exits[direction]
                    self.current_room.describe()
                else:
                    print("You can't go that way.")
            else:
                print("Unknown command")

if __name__ == "__main__":
    game = Game()
    game.start()