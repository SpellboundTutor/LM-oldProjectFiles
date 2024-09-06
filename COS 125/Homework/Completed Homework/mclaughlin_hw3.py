'''Logan McLaughlin
Homework 3: Drawing Pretty Pictures with Python for Fun and Profit
Helps:

Zac Hutchinson (Several times)
Help in COS 125 Lab
Probably help in myriad other places too.

Student notes:

This assignment was extremely difficult, moreso than I thought, and I absolutely noticed how I overcomplicated things initially, using the wrong formulae to come to the complete wrong conclusion.
By some bizarre miracle, I was able to stumble through, but I spent several hours on this homework. Probably 10+ broken up between the time of the homework being assigned until submitting it here.
This was a very stressful assignment as I constantly felt like I lacked the tools I needed to solve the problem a lot of the time, and to my credit with that train of thought, there were tools I
was absolutely missing.

That being said, I absolutely understand why an assignment like this is critical in our class: Mistakes are going to be made when doing something like this that, perhaps, is not something that is
traditionally done in more conventional, casual programming, and it's better to make those serious mistakes now when you are surrounded by so, so many resources available to help you break out of
conventional thinking.

I hate this assignment so much, but I also appreciate what it had to teach us about tackling a relatively abstract project.

'''

import math #required for Square Root
r = int(input("What is the radius of the circle?")) #Getting the radius of the circle
cenX = r #The centermost point of the circle on the X axis
cenY = r # the centermost point of the circle on the Y axis
printX = 0 #Initializing the variable in the For loop to determine the current x position relative to the center.
printY = 0 #Initializing the variable in the For loop to determine the current y position relative to the center.

for y in range(r*2): #For loop to change vertical lines.
    for x in range(r*2): #For loop to change position in horizontal line.
        printX = (x-cenX) #Calculating printX to determine the current x position relative to the center.
        printY = (y-cenY) #Calculating printY to determine the current y position relative to the center.
        d = int((math.sqrt(printX**2 + printY**2))) #Calculating diameter using the square root function from the math module we imported earlier on our relative positions of x and y from earlier.
       # print(f'printX = {printX} || printY = {printY} || d = {d}') #Troubleshooting used by TA in COS 125 lab to determine why certain values were and were not working.

        if d>r:
            print(" ", end="") #If the value of our given diameter exceeds the radius of our circle, blank space will be printed.
        elif ((printX == 0) and (printY == 0)): 
            print("+", end="") #If the value of both of our relative values are 0 distance away from the centermost point, a + will be printed.
        elif (printY == 0):
            print("-", end="") #If only the y value relative to the center is at 0, meaning the 'cursor' is on the x-intercept, a - will be printed.
        elif (printX == 0):
            print("|", end="") #If only the x value relative to the center is at 0, meaning the 'cursor' is on the y-intercept, a | will be printed.
        elif (printY == printX):
            print("\\", end="") #If the relative values of y and x are equal, a \ will be printed. 
        elif (abs(printX)==abs(printY)):
            print("/", end="") #If the relative values of y and x are not equal, but the absolutes of the relative values of y and x are equal, a / will be printed.
        else:
            print("*", end="") #In all other cases, meaning where neither empty space nor a special character needs to be printed, a * will be printed to fill the circle.

    print(" ") #This symbolizes a line break within the loop, as we are using end="" to prevent the line break from happening in our prior print messages.
    x = 0 #This reinitializes our inner x for loop, so as the line progresses down, the 'cursor' will reset back at the far left of our image.
        


