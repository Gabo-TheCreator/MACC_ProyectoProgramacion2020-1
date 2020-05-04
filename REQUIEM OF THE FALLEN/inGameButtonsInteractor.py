from enums import Enums
#A lo largo de la página, se definen:
#Índices de los botones de selección del menú, con sus cambios de estado y con
#posibilidad de pasar al mínimo si se intenta ir más allá del máximo
class inGameButtonsInteractor:

    # Inventory, Attack
    baseButtons = [Enums.inGame.Menu.baseState.Button.inventory,
                   Enums.inGame.Menu.baseState.Button.attack]
    baseButtonsIndex: int = None

    baseMinIndex = 0
    baseMaxIndex = len(baseButtons) - 1

    # Inventory: Health, Mana, Boost, Mana
    inventoryButtons = [Enums.inGame.Menu.inventory.Button.health,
                        Enums.inGame.Menu.inventory.Button.mana,
                        Enums.inGame.Menu.inventory.Button.boost,
                        Enums.inGame.Menu.inventory.Button.empty]
    inventoryButtonsIndex: int = None

    inventoryMinIndex = 0
    inventoryMaxIndex = len(inventoryButtons) - 1

    # Attack: Slash, Magic
    attackButtons = [Enums.inGame.Menu.attack.Button.slash,
                     Enums.inGame.Menu.attack.Button.magic]
    attackButtonsIndex: int = None

    attackMinIndex = 0
    attackMaxIndex = len(attackButtons) - 1

    def __init__(self):
        self.baseButtonsIndex = 0
        self.inventoryButtonsIndex = 0
        self.attackButtonsIndex = 0

    def validateBaseButtonsNewIndexPosition(self, actualIndex, direction=Enums.inGame.Menu.baseState.directions.none):
        print("validateBaseButtonsNewIndexPosition")
        directions = Enums.inGame.Menu.baseState.directions
        updatedIndex: int = None
        minLimit = self.baseMinIndex
        maxLimit = self.baseMaxIndex

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

    def validateInventoryButtonsNewIndexPosition(self,actualIndex, direction=Enums.inGame.Menu.baseState.directions.none):
        directions = Enums.inGame.Menu.inventory.directions
        updatedIndex: int = None
        minLimit = self.inventoryMinIndex
        maxLimit = self.inventoryMaxIndex

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
        elif direction == directions.up or direction == directions.down:
            if actualIndex == minLimit:
                updatedIndex = maxLimit
            else:
                updatedIndex = actualIndex - 1

            if actualIndex == minLimit:
                updatedIndex = maxLimit
            else:
                updatedIndex = actualIndex - 1

        return updatedIndex

    def validateAttackButtonsNewIndexPosition(self,actualIndex, direction=Enums.inGame.Menu.baseState.directions.none):
        directions = Enums.inGame.Menu.attack.directions
        updatedIndex: int = None
        minLimit = self.attackMinIndex
        maxLimit = self.attackMaxIndex

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

        return updatedIndex

