from Character import Character


class ActionMenu:
    thisPlayer = None
    thisEnemy = None
    thisScreen = None

    def __init__(self, player, enemy, screen):
        if player != None and enemy != None and screen != None:
            self.thisPlayer = player
            self.thisEnemy = enemy
            self.thisScreen = screen
