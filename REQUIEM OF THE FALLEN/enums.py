from enum import Enum


# Para todas las enumeraciones necesitamos darles un valor inicial, de lo contrario al momento de saber cual es su valor nos va a retornar None
class Enums:
    class Screens(Enum):
        none = -1
        mainMenu = 0
        selectName = 1
        inGame = 2
        about = 3
        introduction = 4
        confirmExit = 5

    class CharacterType(Enum):
        none = -1
        player = 0
        enemy = 1

    class TextAnimations(Enum):
        none = -1
        typewriter = 0

    class MainMenu:
        class Button(Enum):
            play = 0
            about = 1
            exit = 2

        class directions(Enum):
            none = -1
            right = 0
            left = 1
