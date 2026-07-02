# Kevin
# Handles: Food, Medicine, Bullets, Square Parts, and Clothing
# Displays: Food 125 lbs, Medicine 3, Bullets 50, and Spare Parts 2

class Inventory:

    def __init__(self):
        self.food = 125        # in lbs
        self.medicine = 3
        self.spare_parts = 2
        self.gold = 50
        self.weapons = []      # list of weapon names/strings
        self.poisons = 0
        self.books = []        # list of book names/strings
        self.beast_skin = 0
        self.meat = 0          # in lbs

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
        elif item == "poison":
            self.poisons += amount
        elif item == "beast skin":
            self.beast_skin += amount
        elif item == "meat":
            self.meat += amount
        elif item == "weapon":
            self.weapons.append(amount)   # pass the weapon name as 'amount'
        elif item == "book":
            self.books.append(amount)     # pass the book name as 'amount'
        else:
            print(f"Unknown item: {item}")

    def remove_item(self, item, amount=1):
        """Remove an amount of an item from the inventory."""
        item = item.lower()
        if item == "food" and self.food >= amount:
            self.food -= amount
        elif item == "medicine" and self.medicine >= amount:
            self.medicine -= amount
        elif item == "gold" and self.gold >= amount:
            self.gold -= amount
        elif item == "poison" and self.poisons >= amount:
            self.poisons -= amount
        else:
            print(f"Not enough {item} to remove.")

    def has_item(self, item, amount=1):
        """Check if the inventory has at least a certain amount of an item."""
        item = item.lower()
        if item == "food":
            return self.food >= amount
        elif item == "medicine":
            return self.medicine >= amount
        elif item == "gold":
            return self.gold >= amount
        return False

    def display(self):
        """Print the current inventory to the console."""
        print("\n--- Inventory ---")
        print(f"  Food:        {self.food} lbs")
        print(f"  Medicine:    {self.medicine}")
        print(f"  Spare Parts: {self.spare_parts}")
        print(f"  Gold:        {self.gold}")
        print(f"  Poisons:     {self.poisons}")
        print(f"  Beast Skin:  {self.beast_skin}")
        print(f"  Meat:        {self.meat} lbs")
        print(f"  Weapons:     {', '.join(self.weapons) if self.weapons else 'None'}")
        print(f"  Books:       {', '.join(self.books) if self.books else 'None'}")
        print("-----------------\n")
        
