class ProductManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)
        print(f"New quest added: {quest}")

    def list_quests(self):
        if not self.quests:
            print("No quests available.")
        else:
            print("Current quests:")
            for quest in self.quests:
                print(f"- {quest}")
