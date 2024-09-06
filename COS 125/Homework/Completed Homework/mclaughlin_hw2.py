'''Logan McLaughlin
Homework 2: You Come To A Crossroads
Helps used: None.

Misc Notes: I took the liberty to adjust the lines for clarity and grammar. I know I didn't have to, but the way some dialog boxes were structured tweaked me just a tad.'''

woodPath = input("You are in a strange wood. Paths lead [e]ast and [w]est.\n Which path do you take?") #Ahh, the first choice of a game. East or West> Left or Right? Luxons or Kurzicks?
if woodPath == "e": #If the player goes East
    print("You find an old fire pit. In the ash, you spot a silver key.") #Classic Silver Key glinting in the ashes of a fire.
    has_key = True #The player has a key now!
elif woodPath == "w": #If the player goes west
    print("In a patch of short grass, you find a smooth rock.") #It's... a rock.
    has_rock = True #Congratulations, player. You have a rock. Truly the stuff of legends.

beachPath = input("You arrive at a lonely beach.\n Continue along the [b]each or head [i]nland?") #Not your anime-loving friend's beach episode.
if beachPath == "i": #if we go inland
    print("Inland, the ground becomes marshy. Walking is difficult.") #Should've brought better boots.
    returnPath = input("You may [r]eturn to the beach or [c]ontinue on.") #This should go well.
    if returnPath == "c": #If we continue further.
        print("The water gets depeer and the reeds get higher. You stumble forward recklessly into the hunting ground of saltwater crocodiles.\n GAME OVER: BAD ENDING") #The Captain Hook ending. You hate to see it.

print("The beach seems to go on forever. You're starting to get thirsty, but there's nothing to drink but brackish saltwater.\n After an hour, you come to a small shack build out of driftwood. The door is locked.") #A locked door! The only thing less resistable to a player is a locked chest!
if has_key == True: #Do we have the key?
    useKey = input("You have a Silver Key. Do you use the [k]ey or [l]eave?") #We do! But do we use it?
    if useKey == "k": #The key is used. I hope there's not a miniboss room on the other side.
        print("The Silver Key unlocks the door to the shack. You step inside.") #We step into the darkness.
        openDoor = True #The door is open!
    else:
        openDoor = False #Temptation resisted!
elif has_rock == True: #Dwayne Johnson has joined the party!
    useRock = input("You have a rock. Do you use the [r]ock or [l]eave?") #Do you smell what The Rock is cooking?
    if useRock == "r": #We do!
        print("You hit the door's handle repeatedly with the rock. Eventually, the handle falls off and the force of your last swing causes the door to open.") #Truly, the only civilized response to a locked door.
        openDoor = True #The door is open!
    else:
        openDoor = False #We didn't commit a potential crime!

if openDoor == False: #If we went our own way...
    print("Either because of timidity and fear or respect for private property, you turn your back on the door and walk away. Hours later, you find the highway.\n Within a week, you've forgotten all about the house on the beach.\n GAME OVER: BORING ENDING") #The player is boring for not going along with the plot! Hooray!

if openDoor == True: #We open the door!
    takeDrink = input("Inside, an old man sits in a rocking chair. He is unable or unwilling to talk to you. But, as if able to read your mind, he offers you a bottle to drink.\n Do you [t]ake the bottle from the silent man or [r]efuse his kind offer?") #I've played enough RPGs to see where this is going.
    if takeDrink == "r": #We refuse to take the bottle from the absolutely not telepathic old man with only the most altruistic intentions!
        print("You turn away from the silent man. Eventually you make it back to civilization. For the rest of your life, however, you are haunted by a decision you refused to make.\n GAME OVER: PATHETIC ENDING") #I only wrote the ending was pathetic 'cause the assignment said so? But would you drink a strange liquid from an old man in a shack on a beach? I wouldn't. You'd sooner get poisoned than eternal life.
    elif takeDrink == "t": #We take the bottle from the suspicious old man. Sure.
        useDrink = input("Do you [d]rink the contents of the bottle or [p]our them out into the sand?") #Do you feel lucky? Does exposing yourself to gamma radiation give you Hulk powers?
        if useDrink == "p": #The player makes the correct choice at last.
            print("A syrupy, yellow liquid drains slowly from the bottle. On the ground, it fumes and bubbles, smelling of sulfur.\n As the smoke from the puddle thickens, you catch a disappointed look from the old man. When the smoke clears, he and his shack are gone.\n GAME OVER: WISE ENDING") #Congratulations, you have common sense!
        elif useDrink == "d": #The player likes to live dangerously.
            print("Whatever is in the bottle tastes awful. In seconds, you pass out and fall into the sand of the beach.\n Centuries later, you still remember the smile on the old man's face. You look in the bathroom mirror, staring back at your own face, as young as it was on that fateful day.\n GAME OVER: GOOD ENDING") #This should be renamed the "Lucky Ending".