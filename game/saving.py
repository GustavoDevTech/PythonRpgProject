# Save and load functionality
# Implement Save Function
# Implement Load Function

import os

saveFile = "oregon_trail_save.txt"


def saveGame(player, inventory, distance):
#Save current game state.
    
    file = open(saveFile, "w")
    file.write(str(player.health) + "\n")
    file.write(str(player.moral) + "\n")
    file.write(str(distance) + "\n")
    file.write(str(inventory.gold) + "\n")
    file.write(str(inventory.food) + "\n")
    file.write(str(inventory.map) + "\n")
    file.close()

    print("Game saved successfully!")


def loadGame(player, inventory):
#Load game state. Returns distance or none.
    
    if os.path.exists(saveFile) == False:
        print("No save file found.")
        return None

    file = open(saveFile, "r")
    lines = file.readlines()
    file.close()

    player.health  = int(lines[0])
    player.moral   = int(lines[1])
    distance       = int(lines[2])
    inventory.gold = int(lines[3])
    inventory.food = int(lines[4])
    inventory.map  = int(lines[5])

    print("Game loaded successfully!")
    return distance
