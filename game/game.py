from rooms import Room
from product_manager import ProductManager
from architect import Architect
from engineer import Engineer
from qa_engineer import QAEngineer

class Game:
    def __init__(self):
        self.rooms = {
            'Living Room': Room('Living Room', 'A cozy living room with a fireplace.', ['key', 'map']),
            'Kitchen': Room('Kitchen', 'A kitchen with a strange smell.', ['knife', 'apple']),
            'Bedroom': Room('Bedroom', 'A peaceful bedroom with a comfortable bed.', ['pillow', 'book']),
            'Office': Room('Office room', 'A peaceful bedroom with a comfortable table.', ['Laptop', 'Mobile']),
        }
        self.current_room = self.rooms['Living Room']
        self.rooms['Living Room'].exits = {'north': self.rooms['Kitchen'], 'east': self.rooms['Bedroom']}
        self.rooms['Kitchen'].exits = {'south': self.rooms['Living Room'], 'north': self.rooms['Living Room'],'west': self.rooms['Office'] }
        self.rooms['Bedroom'].exits = {'north': self.rooms['Living Room'],'south': self.rooms['Kitchen'],'west': self.rooms['Office']}
        self.rooms['Office'].exits = {'north': self.rooms['Living Room'],'south': self.rooms['Kitchen'],'west': self.rooms['Bedroom']}

        self.product_manager = ProductManager()
        self.architect = Architect()
        self.engineer = Engineer()
        self.qa_engineer = QAEngineer()


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

            elif command == 'quests':
                self.product_manager.list_quests()
                
            elif command == 'room list':
                print('Rooms:')
                for room_name in self.rooms:
                    print(room_name)


            elif command.startswith('add quest '):
                quest = command[len('add quest '):]
                self.product_manager.add_quest(quest)

            elif command.startswith('add room '):
                parts = command[len('add room '):].split(';')
                print('---',parts)
                room_name = parts[0]
                room_description = parts[1]
                self.architect.add_room(self, room_name, room_description)

            elif command.startswith('add item '):
                parts = command[len('add item '):].split(' to ')
                item = parts[0]
                room_name = parts[1].title()
                if room_name in self.rooms:
                    self.engineer.create_item(self.rooms[room_name], item)
                else:
                    print(f"Room '{room_name}' does not exist.")

            elif command.startswith('verify room '):
                _room_name = command[len('verify room '):]
                room_name = _room_name.title()
                print('My command is ',room_name.title())

                if room_name in self.rooms:
                    self.qa_engineer.verify_room(self.rooms[room_name])
                else:
                    print(f"Room '{room_name}' does not exist.")

            else:
                print("Unknown command")


    # def start(self):
    #     print("Welcome to the Adventure Game!")
    #     self.current_room.describe()
    #     while True:
    #         command = input("> ").strip().lower()
    #         if command in ['quit', 'exit']:
    #             print("Thanks for playing!")
    #             break
    #         elif command == 'look':
    #             self.current_room.describe()
    #         elif command.startswith('go '):
    #             direction = command.split()[1]
    #             if direction in self.current_room.exits:
    #                 self.current_room = self.current_room.exits[direction]
    #                 self.current_room.describe()
    #             else:
    #                 print("You can't go that way.")
    #         elif command == 'quests':
    #             self.product_manager.list_quests()
    #         elif command.startswith('add quest '):
    #             quest = command[len('add quest '):]
    #             self.product_manager.add_quest(quest)
    #         # elif command.startswith('add room '):
    #         #     parts = command[len('add room '):].split(';')
    #         #     print('---',parts)
    #         #     room_name = parts[0]
    #         #     room_description = parts[1]
    #         #     self.architect.add_room(self, room_name, room_description)
    #         # elif command.startswith('add item '):
    #         #     parts = command[len('add item '):].split(' to ')
    #         #     item = parts[0]
    #         #     room_name = parts[1]
    #         #     if room_name in self.rooms:
    #         #         self.engineer.create_item(self.rooms[room_name], item)
    #         #     else:
    #         #         print(f"Room '{room_name}' does not exist.")
    #         elif command.startswith('verify room '):
    #             room_name = command[len('verify room '):]
    #             if room_name in self.rooms:
    #                 self.qa_engineer.verify_room(self.rooms[room_name])
    #             else:
    #                 print(f"Room '{room_name}' does not exist.")
    #         else:
    #             print("Unknown command")

if __name__ == "__main__":
    game = Game()
    game.start()