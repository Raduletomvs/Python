class JungleAnimal:
    def __init__(self, animal_name, age, sound):
        self.animal_name = animal_name
        self.age = age
        self.sound = sound
    
    def __str__(self):
        return f"{self.animal_name} {self.age} {self.sound}"
 
    def __repr__(self):
        return f"{self.animal_name} {self.age} {self.sound}"
 
class InvalidParameterError:
    try:
        pass
    except InvalidAgeError:
        pass
    except InvalidSoundError:
        pass
 
data = [
JungleAnimal("Lizzy", 14, "Shriek"), 
JungleAnimal("Lorelei", 13, "Meow"), 
JungleAnimal("Abigail", 16, "Meow"),
JungleAnimal("Mac", 9, "ROAR"),
JungleAnimal("Lizzy", 11, "Aaaaa"), 
JungleAnimal("Susan", 16, "Shriek")
]