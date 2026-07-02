# Yazir
# Random Text Hunting: Use random
# Allows the player to hunt for food.
# Uses random outcomes to determine success.
# Updates food, bullets, and health
# Random Text Hunting
# lets the player hunt for food
# uses random numbers to figure out if it works or not
# changes food, bullets, and health
# also has a really rare item you can find while hunting

import random

def hunt(player, inventory):
    
    if inventory.bullets <= 0:
        print("You dont have any bullets left, cant hunt right now")
    else:
        inventory.bullets -= 1
        outcome = random.randint(1, 10)
        
        if outcome == 1:
            food = random.randint(20, 40)
            inventory.food += food
            print("You shot a deer! You got " + str(food) + " lbs of food")
            
        elif outcome == 2:
            food = random.randint(20, 40)
            inventory.food += food
            print("You shot a deer! You got " + str(food) + " lbs of food")
            
        elif outcome == 3:
            food = random.randint(20, 40)
            inventory.food += food
            print("You shot a deer! You got " + str(food) + " lbs of food")
            
        elif outcome == 4:
            food = random.randint(20, 40)
            inventory.food += food
            print("You shot a deer! You got " + str(food) + " lbs of food")
            
        elif outcome == 5:
            food = random.randint(5, 15)
            inventory.food += food
            print("You shot a rabbit, not much but you got " + str(food) + " lbs of food")
            
        elif outcome == 6:
            food = random.randint(5, 15)
            inventory.food += food
            print("You shot a rabbit, not much but you got " + str(food) + " lbs of food")
            
        elif outcome == 7:
            food = random.randint(5, 15)
            inventory.food += food
            print("You shot a rabbit, not much but you got " + str(food) + " lbs of food")
            
        elif outcome == 8:
            print("The animal ran away before you could shoot it. You got nothing")
            
        elif outcome == 9:
            print("You walked around for hours and didnt find anything to hunt")
            player.morale -= 5
            
        else:
            damage = random.randint(5, 15)
            player.health -= damage
            print("You tripped and hurt yourself while hunting, lost " + str(damage) + " health")
        
        print("Bullets left: " + str(inventory.bullets))
        print("Food: " + str(inventory.food))
        print("Health: " + str(player.health))
        
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
