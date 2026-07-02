# Lucchino
# Random Things Happening
# Example1: A wagon wheel broke. A member became ill. 
# Example2: You found berries. A storm damaged supplies. You met another traveler. 

import random

def randomevent(player, inventory):
    event = random.randint(1, 14)
    
    if event == 1:
        print("You got sick, you start throwing up")
        player.health -= 15
        
    elif event == 2:
        print("You found a pouch full of gold coins")
        inventory.gold += 2
    
    elif event == 3:
        print("You found a new map")
        inventory.map += 1
        
    elif event == 4:
        print("A wheel on the wagon broke")
        player.distance += 15
    
    elif event == 5:
        print("Someone appears out of nowhere and steals your water supply.")
        player.health -= 20
        
    elif event == 6:
        print("A wise person appears to you and gives you advice about your journey and your destination.")
        player.morale += 15
    
    elif event == 7:
        print("You found an old mysterious tavern called “Ravenscross” ")
        player.health += 5
        inventory.food += 5
        player.morale += 5
        inventory.gold -= 5
        
    elif event == 8:
        print("You run into the blacksmith from “Emberhollow” ")
        player.morale += 5
    
    elif event == 9:
        print("You come across a marketplace and trade for gold")
        inventory.gold += 10
        inventory.food -= 7
        
    elif event == 10:
        print("You have found an oasis")
        player.health += 15
        inventory.food += 10
        player.morale += 10
        
    elif event == 11:
        print("You found a toolbox")
        inventory.tools += 5
        
    elif event == 12:
        print("A severe thunderstorm approaches")
        player.morale -= 10
        player.health -= 5
        
    elif event == 13:
        print("Bad luck, you twisted your ankle")
        player.morale -= 10
        player.distance += 10
        player.health -= 10
        
    else:
        print("Nothing Happened")
        
