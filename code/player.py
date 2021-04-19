class Player:
    Pv = 10
    atk = 3
    Def = 5

Inventory = []

    def __init__(self,role):
        if role == "Warrior":
            self.Pv = 20
            self.atk = 5
            self.Def = 10
        elif role =="Mage":
            self.Pv = 10
            self.atk = 10
            self.Def = 5


    def Damage(self,dmg):
        dmg = dmg - self.Def
        self.Pv -= dmg 

    def print_Inventory(self):
        for item in self.Inventory:
            print(item)