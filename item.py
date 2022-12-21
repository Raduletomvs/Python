class Item:
    def __init__(self, name, durability, attack=None):
        self.name = name
        self.durability = durability
        self.attack = attack

    def __repr__(self):
        attack_str = str(self.attack) if self.attack is not None else "None"
        return f"Item({self.name}, {self.durability}, {attack_str})"