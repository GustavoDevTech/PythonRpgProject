"""
Handles: Moving Forward, Distance Calculations,
Choosing Pace, and Resting.
Examples: Continue Traveling. Rest. Change Pace. Check Inventory

travel.py

Travel System: Gustavo

Handles:
- Difficulty
- Traveling
- Resting
- Calendar
- Distance
"""

import random

# -----------------------------------
# Month Names
# -----------------------------------

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


MONTH_LENGTH = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}


# -----------------------------------
# Difficulty Selection
# -----------------------------------

def choose_difficulty(player, inventory):

    print("\n===== Difficulty =====")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    print("4. Impossible")

    while True:

        choice = input("Choose Difficulty: ")

        if choice == "1":

            inventory.food = 1000
            player.health = 100
            player.max_health = 100

            print("\nEasy difficulty selected.")
            break

        elif choice == "2":

            inventory.food = 750
            player.health = 100
            player.max_health = 100

            print("\nNormal difficulty selected.")
            break

        elif choice == "3":

            inventory.food = 500
            player.health = 80
            player.max_health = 80

            print("\nHard difficulty selected.")
            break

        elif choice == "4":

            inventory.food = 250
            player.health = 60
            player.max_health = 60

            print("\nImpossible difficulty selected.")
            break

        else:

            print("Invalid choice. Try again.")
            
# -----------------------------------
# Calendar System
# -----------------------------------

def advance_days(player, days):

    player.day += days

    while player.day > MONTH_LENGTH[player.month]:

        player.day -= MONTH_LENGTH[player.month]
        player.month += 1

        if player.month > 12:
            player.month = 1


def get_month_name(player):

    return MONTHS[player.month]


# -----------------------------------
# Display Travel Status
# -----------------------------------

def display_status(player, inventory):

    print("\n===================================")
    print("        MEDIEVAL TRAIL")
    print("===================================")

    print(f"Date: {get_month_name(player)} {player.day}")
    print(f"Distance Traveled: {player.distance} miles")

    print("-----------------------------------")

    print(f"Health : {player.health}/{player.max_health}")
    print(f"Morale : {player.morale}/{player.max_morale}")

    print("-----------------------------------")

    print(f"Food : {inventory.food} lbs")
    print(f"Gold : {inventory.gold}")

    print("===================================")


# -----------------------------------
# Travel
# -----------------------------------

def travel(player, inventory):

    miles = random.randint(30, 60)

    player.distance += miles

    food_used = random.randint(8, 15)

    inventory.food -= food_used

    days = random.randint(3, 7)

    advance_days(player, days)

    player.days_traveled += days

    print("\nYou traveled", miles, "miles.")

    print("Food Consumed:", food_used)

    print(days, "days have passed.")

    if inventory.food < 0:
        inventory.food = 0


# -----------------------------------
# Rest
# -----------------------------------

def rest(player):

    heal = random.randint(5, 15)

    player.health += heal

    if player.health > player.max_health:
        player.health = player.max_health

    days = random.randint(2, 5)

    advance_days(player, days)

    player.rests += 1

    print("\nYou rested.")

    print("Recovered", heal, "health.")

    print(days, "days have passed.")
    
# -----------------------------------
# Check Player Status
# -----------------------------------

def check_player(player, inventory):

    if player.health <= 0:
        print("\nYou have died on your journey...")
        return False

    if inventory.food <= 0:
        print("\nYou have run out of food!")
        print("Your group begins to starve.")

        player.health -= 10

        if player.health <= 0:
            print("Everyone has perished from starvation.")
            return False

    return True


# -----------------------------------
# Check Victory
# -----------------------------------

def reached_destination(player):

    GOAL_DISTANCE = 1000

    if player.distance >= GOAL_DISTANCE:
        return True

    return False


# -----------------------------------
# Main Travel Menu
# -----------------------------------

def travel_menu():

    print("\n========== Travel Menu ==========")
    print("1. Continue Traveling")
    print("2. Rest")
    print("3. Hunt")
    print("4. View Inventory")
    print("5. Save Game")
    print("6. Quit Game")

    choice = input("Choose an option: ")

    return choice    
