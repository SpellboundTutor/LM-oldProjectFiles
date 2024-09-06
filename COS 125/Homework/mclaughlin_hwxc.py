# Logan McLaughlin
# Homework XC:
# Helps Used:

import sys

cmdraw = open(sys.argv[1])
# cmdraw = "0011D9R5R4U8LLLLLLLL" #Test Only
cmdrevised = [] #list to convert list of characters into revised list, converting number strings to integers.
cmdcommands = [] #list to convert revised data into lists of commands.
cmdlist = list(cmdraw) #converts raw data into a list of characters.
cmdstart = cmdlist[0:2] #slices the first two characters as the start coordinates, x and y.
cmdend = cmdlist[2:4] #slices the next two characters as the end coordinates, x and y
integers = [0,1,2,3,4,5,6,7,8,9] #I don't remember if there's a better way to do this, so I just made a list of integers 0-9 for checking.


for i in range(len(cmdlist[4:])): #This will run for every character in our list and converts number strings into integers.
    try:
        cmdrevised.append(int(cmdlist[i])) #Tries to revise a character at i into an integer.
    except ValueError:
        cmdrevised.append(cmdlist[i]) #If it can't, just leaves it alone.

for i in range(len(cmdrevised)): #This will pair off any commands as necessary.
    if isinstance(cmdrevised[i], str): #If cmdrevised[i] is a string...
        try:
            if isinstance(cmdrevised[i+1], int): #If the value in the pair exists and is an integer, it will try to turn both values into its own list.
                cmdcommands.append([cmdrevised[i], cmdrevised[i+1]])
            else: 
                cmdcommands.append([cmdrevised[i]]) #If the value in the pair exists, but is not an integer, it won't.
        except IndexError:
            cmdcommands.append([cmdrevised[i]]) #If the value in the pair does not exist, it will just return the string by itself.


cmdstart = cmdrevised[0:2] #slices the first set of coordinates of the revised command list.
cmdend = cmdrevised[2:4] #slices the second set of coordinates of the revised command list.

boardx = 10 #sets the size of the board x
boardy = 10 #sets the size of the board y
startx = cmdstart[0] #sets the starting x coordinate
starty = cmdstart[1] #sets the starting y coordinate
endx = cmdend[0] #sets the ending x coordinate
endy = cmdend[1] #sets the ending y coordinate
stepx = startx #sets the step x coordinate equal to the start coordinate. This will be used to track steps.
stepy = starty #sets the step y coordinate equal to the start coordinate. This will be used to track steps.

for i in range(len(cmdcommands)):
    if cmdcommands[i][0] == "U": #If the command has us going Up...
        try:
            stepy += cmdcommands[i][1] #If it's going Up by a determined value, the step count for y will increase by that amount.
        except IndexError:
            stepy += 1 #If there is no determined value, it goes up by 1.
    elif cmdcommands[i][0] == "D": #If the command has us going Down...
        try:
            stepy -= cmdcommands[i][1] #If it's going Down by a determined value, the step count for y will decrease by that amount.
        except IndexError:
            stepy -= 1 #Otherwise, goes down by 1
    elif cmdcommands[i][0] == "L": #If we're going Left...
        try:
            stepx -= cmdcommands[i][1] #Decreases x by a value if the value exists.
        except IndexError:
            stepx -= 1 #Otherwise decreases by 1
    elif cmdcommands[i][0] == "R": #If we're going Right...
        try:
            stepx += cmdcommands[i][1] #Increases x by a value if the value exists.
        except IndexError:
            stepx += 1 #Otherwise increases by 1
    else:
        continue
    if stepx > boardx: #If the step would take us beyond the bounds of the board from the right...
        stepx = boardx - stepx #set the step counter to the opposite side of the board.
    elif stepx < 0: #If the step would take us beyond the bounds of the board from the left...
        stepx = boardx + stepx #Set the step counter to the opposite side of the board.
    if stepy > boardy: #If the step counter would take us beyond the bounds of the board from the top...
        stepy = boardy - stepy #Set the step counter to the opposite side of the board.
    elif stepy < 0: #If the step counter would take us beyond the bounds of the board from the bottom...
        stepy = boardy + stepy #Set the step counter to the opposite side of the board.

print(f"Start: {startx}, {starty}\n End: {endx}, {endy}\n Final: {stepx}, {stepy}") #Print our Start coords, stop coords, and final coords.
if stepx == endx: #If the x coordinate for our step is the same as our end step...
    if stepy == endy: #AND if the y coordinate for our step is the same as our end step...
        print("OK") #Print OK! You win!
    else:
        print("KO") #Y coordinate doesn't match. Game over!
else:
    print("KO") #X coordinate doesn't match. Game over!
