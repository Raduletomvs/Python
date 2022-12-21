import errors , entity

class Menu:
    def __init__(self):
        self.characters = {}

    def create_character(self):
        name = input("Enter character name (at least 4 characters): ")
        if name in self.characters:
            raise errors.CharacterExists(f"Character with name '{name}' already exists")
        gender = input("Enter gender (M or F): ")
        if gender not in ("M", "F"):
            raise errors.InvalidDataFormat("Invalid gender format")
        char_class = input("Enter character class (Warrior, Mage, Priest, Rogue): ")
        if char_class not in ("Warrior", "Mage", "Priest", "Rogue"):
            raise errors.InvalidCharacterClass("Invalid character class")
        character = entity.Character(name, gender, char_class)
        self.characters[name] = character
        print(f"Character '{name}' created successfully")

class Character:
    def __init__(self, name, gender, char_class, weapon=None, additional_item=None):
        self.name = name
        self.gender = gender
        self.char_class = char_class
        self.weapon = weapon
        self.additional_item = additional_item

    def __repr__(self):
        weapon_str = self.weapon.__repr__() if self.weapon is not None else "None"
        item_str = self.additional_item.__repr__() if self.additional_item is not None else "None"
        return f"Character({self.name}, {self.gender}, {self.char_class}, {weapon_str}, {item_str})"