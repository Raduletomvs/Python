import errors , entity

class Weapon:
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