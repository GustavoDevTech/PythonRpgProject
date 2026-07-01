# Brienne
# Tracks: Health, Morale,

import random


health = 100
max_health = 100
moral = 100
max_moral = 100

print(f"Starting Health! Player HP: {health}/{max_health}\n")
print(f"Starting Moral! Player Moral: {moral}/{max_moral}\n")

while health > 0:
        print("\nChoose an action:")
        print("1. Take damage")
        print("2. Heal")
        print("3. Lose moral")
        print("4. Heal moral")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            damage = random.randint(5, 20)
            health -= damage
            health = max(health, 0) 
            print(f"💥 Took {damage} damage! HP: {health}/{max_health}")

        elif choice == "2":
            heal = random.randint(5, 15)  
            health += heal
            health = min(health, max_health) 
            print(f"❤ Healed {heal} HP! HP: {health}/{max_health}")

        elif choice == "3":
            damage = random.randint(5, 20)
            moral -= damage
            moral = max(moral, 0) 
            print(f"🧠 Lost {damage} moral! Moral: {moral}/{max_moral}")

        else:
            heal = random.randint(5, 15)  
            moral += heal
            moral = min(moral, max_moral) 
            print(f"❤ Healed {heal} moral! Moral: {moral}/{max_moral}")


print("\n💀 The Player is Dead! Game Over.")
