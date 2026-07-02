# Yazir
# Random Text Hunting: Use random
# Allows the player to hunt for food.
# Uses random outcomes to determine success.
# Updates food, bullets, and health
import random

def hunt(player, inventory):
    
    if inventory.bullets <= 0:
        print("You dont have any bullets left, cant hunt right now")
    else:
        inventory.bullets -= 1
        outcome = random.randint(1, 2)
        
        if outcome == 1:
            food = random.randint(15, 35)
            inventory.food += food
            print("You got a shot off and hit the animal! You got " + str(food) + " lbs of meat")
        else:
            print("You took the shot but missed. The animal ran off, you got nothing")
        
        print("Bullets left: " + str(inventory.bullets))
        print("Food: " + str(inventory.food))
        
      
        rareRoll = random.randint(1, 200)
        if rareRoll == 1:
            if inventory.sign_in_sheet == 0:
                inventory.sign_in_sheet = 1
                player.morale += 30
                player.max_health += 10
                player.health += 10
                print("\nWhile out hunting you find a strange piece of paper stuck in the bushes... its Professor Agars Sign In Sheet!")
                print("Just holding onto it makes you feel unstoppable. Morale and max health went up.")
            else:
                print("You find another Professor Agars Sign In Sheet but you already have one so you leave it")


def forage(player, inventory):
    
    find = random.randint(1, 3)
    
    if find == 1:
        print("You find some berries and eat some before checking if they were safe... turns out they were poisonous")
        damage = random.randint(10, 25)
        player.health -= damage
        print("You lost " + str(damage) + " health")
        
    elif find == 2:
        food = random.randint(5, 20)
        inventory.food += food
        print("You find some berries and they turn out to be safe to eat. You got " + str(food) + " lbs of food")
        
    else:
        inventory.tools += 1
        print("You find some sharp rocks good for making spearheads. Tools went up")
    
    print("Food: " + str(inventory.food))
    print("Health: " + str(player.health))
