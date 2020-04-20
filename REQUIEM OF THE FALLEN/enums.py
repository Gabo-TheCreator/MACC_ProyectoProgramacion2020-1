from enum import Enum


# Para todas las enumeraciones necesitamos darles un valor inicial, de lo contrario al momento de saber cual es su valor nos va a retornar None
class Enums:
    class Screens(Enum):
        none = -1
        mainMenu = 0
        selectName = 1
        inGame = 2
        about = 3
        confirmExit = 4

    class CharaterType(Enum):
        none = -1
        player = 0
        enemy = 1