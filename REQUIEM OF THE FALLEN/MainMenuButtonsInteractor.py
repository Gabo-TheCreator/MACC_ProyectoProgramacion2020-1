from enums import Enums


class MainMenuButtonsInteractor:
    # Actions Buttons
    buttons = [Enums.MainMenu.Button.play.name,
               Enums.MainMenu.Button.about.name,
               Enums.MainMenu.Button.exit.name]
    buttonIndex: int = None

    minIndex = 0
    maxIndex = len(buttons) - 1

    def __init__(self):
        self.buttonIndex = 0

    def validateNewIndexPosition(self, actualIndex, direction=Enums.MainMenu.directions.none):
        directions = Enums.MainMenu.directions
        updatedIndex: int = None
        minLimit = self.minIndex
        maxLimit = self.maxIndex

        if direction == directions.left:
            if actualIndex == minLimit:
                updatedIndex = maxLimit
            else:
                updatedIndex = actualIndex - 1

        elif direction == directions.right:
            if actualIndex == maxLimit:
                updatedIndex = minLimit
            else:
                updatedIndex = actualIndex + 1

        elif direction == directions.none:
            updatedIndex = actualIndex

        return updatedIndex