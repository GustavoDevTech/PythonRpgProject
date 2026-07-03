# Brienne
# Tracks: Health, Morale,

# Changing the attributes inside the Player class
# Changed the structure

import random

class Player:
    
    def __init__(self):
        
        self.health = 100
        self.max_health = 100
        
        self.morale = 100
        self.max_morale = 300
        
    def take_damage(self):
        
        damage = random.randint(5,20)
        
        self.health -= damage
        
        self.health = max(self.health,0)
        
        print(f"💥 Took {damage} damage! HP: {self.health}/{self.max_health}")
        
    def heal(self):
        
        heal = random.randint(5,15)
        
        self.health += heal
        
        self.health = min(self.health,self.max_health)
        
        print(f"❤ Healed {heal} HP! HP: {self.health}/{self.max_health}")
        
    def lose_morale(self):
        
        damage = random.randint(5, 20)
        
        self.morale -= damage
        
        self.morale = max(self.morale,0)
        
        print(f"🧠 Lost {damage} morale! Morale: {self.morale}/{self.max_morale}")
