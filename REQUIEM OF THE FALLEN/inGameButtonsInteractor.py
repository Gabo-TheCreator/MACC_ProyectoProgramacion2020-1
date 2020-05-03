from enums import Enums

class inGameButtonsInteractor:

    # Inventory, Attack
    baseButtons = [Enums.inGame.Menu.baseState.dire]
    baseButtonsIndex: int = None

    baseMinIndex = 0
    baseMaxIndex = len(baseButtons) - 1

    # Inventory: Health, Mana, Boost, Mana
    inventoryButtons = []
    inventoryButtonsIndex: int = None

    inventoryMinIndex = 0
    inventoryMaxIndex = len(inventoryButtons) - 1

    # Attack: Slash, Magic
    attackButtons = []
    attackButtonsIndex: int = None

    attackMinIndex = 0
    attackMaxIndex = len(attackButtons) - 1

    def validateBaseButtonsNewIndexPosition(self, actualIndex, direction=Enums.inGame.Menu.baseState.directions.none):
        print("validateBaseButtonsNewIndexPosition")
        directions = Enums.inGame.Menu.baseState.directions
        updatedIndex: int = None
        minLimit = self.baseMinIndex
        maxLimit = self.baseMaxIndex