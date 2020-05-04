class Ataque:
    dano: int = None
    costoDeMana: int = None
    nombre: str = None
    boost: float = None

    def __init__(self, dano, costoDeMana, nombre, boost):
        print("Creating an Attack")
        self.dano = dano
        self.costoDeMana = costoDeMana
        self.nombre = nombre
        self.boost = boost

    def getDamage(self):
        return self.dano

    def getManaCost(self):
        return self.costoDeMana

    def getName(self):
        return self.nombre

    def getBoost(self):
        return self.boost

#Definición de los argumentos que toman los ataques