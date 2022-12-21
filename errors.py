class GameError(Exception):
    pass

class InvalidCommand(GameError):
    pass

class InvalidDataFormat(GameError):
    pass

class InvalidCharacterClass(GameError):
    pass

class CharacterNotFound(GameError):
    pass

class CharacterExists(GameError):
    pass