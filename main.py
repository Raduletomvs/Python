import entity , errors

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

    def create_weapon(self):
        name = input("Enter character name: ")
        character = self.characters.get(name)
        if character is None:
            raise errors.CharacterNotFound(f"Character with name '{name}' not found")
        weapon_name = input("Enter weapon name (at least 4 characters): ")
        attack = input("Enter attack points (positive integer): ")
        try:
            attack = int(attack)
            if attack <= 0:
                raise ValueError
        except ValueError:
            raise errors.InvalidDataFormat("Invalid attack points format")
        weapon = entity.Item(weapon_name, 100, attack=attack)
        character.weapon = weapon
        print(f"Weapon '{weapon_name}' added to character '{name}'")

    def create_item(self):
        name = input("Enter character name: ")
        character = self.characters.get(name)
        if character is None:
            raise errors.CharacterNotFound(f"Character with name '{name}' not found")
        item_name = input("Enter item name (at least 4 characters): ")
        item = entity.Item(item_name, 100)
        character.additional_item = item
        print(f"Item '{item_name}' added to character '{name}'")

    def print_characters(self):
        if not self.characters:
            print("No characters to print")
        else:
            for character in self.characters.values():
                print(character)

    def delete_character(self):
        name = input("Enter character name: ")
        character = self.characters.pop(name, None)
        if character is None:
            raise errors.CharacterNotFound(f"Character with name '{name}' not found")
        print(f"Character '{name}' deleted successfully")

    def print_commands(self):
        print("1. Create new character")
        print("2. Create a weapon on an existing character")
        print("3. Create an additional item on an existing character")
        print("4. Print all characters")
        print("5. Delete an existing character")

    def run(self):
        while True:
            self.print_commands()
            command = input("Enter command number: ")
            try:
                command = int(command)
                if command == 1:
                    self.create_character()
                elif command == 2:
                    self.create_weapon()
                elif command == 3:
                    self.create_item()
                elif command == 4:
                    self.print_characters()
                elif command == 5:
                    self.delete_character()
                elif command == 6:
                    break
                else:
                    raise errors.InvalidCommand("Invalid command number")
            except errors.GameError as e:
                print(f"Error: {e}")
