# Kevin
# Handles: Food, Medicine, Bullets, Square Parts, and Clothing
# Displays: Food 125 lbs, Medicine 3, Bullets 50, and Spare Parts 2

class Inventory:
    
    def __init__(self):
        # Supplies
        self.food = 125
        self.gold = 50
        self.medicine = 3
        self.spare_parts = 2
        
        # Travel Supplies
        self.tools = 2
        self.bullets = 20
        self.map = 0
        
        # Special Items
        self.sign_in_sheet = 0
        self.poisons = 0
        self.beast_skin = 0
        self.meat = 0
        
        # Collections
        self.weapons = []
        self.books = []
        
    def add_item(self, item, amount=1):
        """Add an amount of an item to the inventory."""
        
        item = item.lower()
        
        if item == "food":
            self.food += amount
            
        elif item == "medicine":
            self.medicine += amount
            
        elif item == "spare parts":
             self.spare_parts += amount
            
        elif item == "gold":
            self.gold += amount
            
        elif item == "tools":
            self.tools += amount
            
        elif item == "bullets":
            self.bullets += amount
            
        elif item == "map":
            self.map += amount
            
        elif item == "sign_in_sheet":
            self.sign_in_sheet += amount
            
        elif item == "poison":
            self.poisons += amount
            
        elif item == "beast skin":
            self.beast_skin += amount
            
        elif item == "meat":
            self.meat += amount
            
        elif item == "weapon":
            self.weapons.append(amount)
            
        elif item == "book":
            self.books.append(amount)
            
        else:
            print(f"Unknown item: {item}")
            
    def remove_item(self, item, amount=1):
        """Remove an amount of an item from the inventory"""
        
        item = item.lower()
        
        if item == "food" and self.food >= amount:
            self.food -= amount
            
        elif item == "medicine" and self.medicine >= amount:
            self.medicine -= amount
            
        elif item == "spare parts" and self.spare_parts >= amount:
            self.spare_parts -= amount
            
        elif item == "gold" and self.gold >= amount:
            self.gold -= amount
            
        elif item == "tools" and self.tools >= amount:
            self.tools -= amount
            
        elif item == "bullets" and self.bullets >= amount:
            self.bullets -= amount
        
        elif item == "map" and self.map >= amount:
            self.map -= amount
            
        elif item == "sign_in_sheet" and self.sign_in_sheet >= amount:
            self.sign_in_sheet -= amount
            
        elif item == "poison" and self.poisons >= amount:
            self.poisons -= amount
            
        elif item == "beast skin" and self.beast_skin >= amount:
            self.beast_skin -= amount
            
        elif item == "meat" and self.meat >= amount:
            self.meat -= amount
            
        else:
            print(f"Not enough {item} to remove.")
            
    def has_item(self, item, amount=1):
        """Check if the inventory has at least a certain amount."""

        item = item.lower()

        if item == "food":
            return self.food >= amount

        elif item == "medicine":
            return self.medicine >= amount

        elif item == "gold":
            return self.gold >= amount

        elif item == "spare parts":
            return self.spare_parts >= amount

        elif item == "tools":
            return self.tools >= amount

        elif item == "bullets":
            return self.bullets >= amount

        elif item == "map":
            return self.map >= amount

        elif item == "sign_in_sheet":
            return self.sign_in_sheet >= amount

        elif item == "poison":
            return self.poisons >= amount

        elif item == "beast skin":
            return self.beast_skin >= amount

        elif item == "meat":
            return self.meat >= amount

        return False

    def display(self):
        """Print the current inventory."""

        print("\n========== INVENTORY ==========")

        print(f"Food:              {self.food} lbs")
        print(f"Medicine:          {self.medicine}")
        print(f"Gold:              {self.gold}")
        print(f"Spare Parts:       {self.spare_parts}")
        print(f"Tools:             {self.tools}")
        print(f"Bullets:           {self.bullets}")
        print(f"Maps:              {self.map}")

        print(f"Poisons:           {self.poisons}")
        print(f"Beast Skin:        {self.beast_skin}")
        print(f"Meat:              {self.meat} lbs")
        print(f"Sign In Sheet:     {'Yes' if self.sign_in_sheet else 'No'}")

        print(f"Weapons:           {', '.join(self.weapons) if self.weapons else 'None'}")
        print(f"Books:             {', '.join(self.books) if self.books else 'None'}")

        print("===============================\n")
        
