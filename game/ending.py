# Cristina
# Determines: Prologues and epilogues. Did the player survive? Did they reach their destination? What ending do they receive?

def Prologue(): #ONCE UPON A TIME
    return"\nYou wake up in the Emberhollow Inn. You’ve been traveling for quite some time now, and you’re beginning to run out of money. You’ve been hearing other travelers talk about getting quick cash by taking quests at the local tavern. Ravencross Tavern, I believe it’s called. You grab the little supplies you still have, and begin to head across the square."
    
def ending1(): #denies the quest
    return "\nYou reject the quest. \n\nYou will surely find some other way to make some money, but not in this game.\n\n ---------- Game Over ---------- \n\nEnding 1/7"
    
def ending2():  #mauled by a beast
    return"The beast’s claws tear through your abdomen, blood splattering onto the nearby trees. You tumble backwards as it lunges towards you. Its jaws latch onto your neck and you can no longer breathe. You feel blinding pain, and then you feel nothing at all. \n\n ---------- Game Over ---------- \n\nEnding 2/7"
    
def ending3(): #robbed by thieves and killed
    return"You feel an agonizing pain in your left side. One of the thieves had come up behind you and stabbed you with a poisoned blade. Your head is spinning and you know you’ve lost. You fall to the ground and you beg for mercy. They grant it. They turn your face toward the beautiful sky as they slit your throat. The thieves stay silent as you go, the only things you can hear sre the birds. \n\n ---------- Game Over ---------- \n\nEnding 3/7"
    
def ending4(): #dies of starvation
    return "\nYou have chosen not to hunt or forage. \n\nYou wander aimlessly through the woods for days and days. You get so hungry and tired that you begin to hallucinate. You stumble upon some berries in a bush. You think you're eating the most delicious blackberries you've ever had, but you're actually eating deadly nightshade. Your heart races, and your chest begins to ache. You feel yourself fall to the floor and then everything goes numb. \n\n ----------- Game Over ---------- \n\nEnding 4/7"
    
def ending5(): #drinks from the fountain
      return"\nYou drink from the Fountain of Eternal Youth.\n\nThe pains in your body that you had learned to ignore began to disappear. The crinkles near your eyes and mouth smooth themselves over. The freckles on your arms from being in the sun fade before your eyes. \n\nYou fill the flask ____ gave you, and you begin your journey home. It was much calmer than the journey here, only stopping to eat and rest. When you finally reach Ravencross Tavern, ____ seems overjoyed. When he sees the flask in your hand, he immediately begins to retrieve the gold you are owed and begins to hand it to you. You bid him farewell and begin your journey to the next kingdom.\n\nCenturies pass. Everyone you have ever loved dies as you stay youthful. You see the rise and fall of technology. You survive plagues, famines, and wars. You notice how history repeats itself constantly. You watch power-hungry maniacs destroy the only planet they can call home. \n\nEventually, a black hole will eat most of the Milky Way. Your body will be constantly tearing itself apart and coming back together. All you will know is agonizing pain. There will be nothing in the galaxy but you and the other morons who drank the water from the fountain. The fountain itself dried out a decade or three after you found it; that drought destroyed most of Pandora. It is a good thing that you didn’t have your loved ones drink from the fountain. They would have hated you by century four, the same way you hated yourself.  \n\n ----------- Game Over ---------- \n\nEnding 5/7"

def ending6(): #does not drink from the fountain
    return"\nYou do not drink from the fountain. \n\nEternal life sounds awful, anyway. You fill the flask ____ gave you, and you begin your journey home. It was much calmer than the journey here, only stopping to eat and rest. When you finally reach Ravencross Tavern, ____ seems overjoyed. When he sees the flask in your hand, he immediately begins to retrieve the gold you are owed and begins to hand it to you. You bid him farewell and begin your journey to the next kingdom.\n\nMany years after the quest, you settle down. You choose a place to live, you garden, you care for animals, and you die peacefully knowing you are cared for by many. \n\n ----------- Game Over ---------- \n\nEnding 6/7"

def ending7(): #gets lost completely
    return"\nYou’re very lost.\n\n After days of struggling, you give up on the quest. You build a shelter, you hunt, you forage, and you stay in the forest. At some point, the people of Emberhollow will talk about you like you're some sort of cryptid. It doesn’t matter, though; now you can serve as a warning for those who are foolish enough to seek eternal youth. Eventually, you will pass, never knowing your house was only 2 more miles from your shelter.\n\n ----------- Game Over ---------- \n\nEnding 7/7"
