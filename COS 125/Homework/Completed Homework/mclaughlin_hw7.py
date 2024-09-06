'''
Logan McLaughlin
Homework 7: The Language of Blah-dee-blah-blah-blah
Helps used: Zac helped, went off to google for some small things, which pointed me to Stack Overflow, etc.
Comments: Tried a bunch of things. Most stuff I actually looked up on google were problems I wasn't even meant to solve.
Made things more complicated than they really should have been. The hints at the bottom of the homework pdf helped a lot!'''

import sys
# print(sys.argv[1]) #reads cmd line
cmdlist = open(sys.argv[1]) #use terminal to open the test file
# cmdlist = open("prog1", "r") #Lazy mode testing
cmdlists = [] #initialize cmdlists as list
cmdlists = cmdlist.readlines() #put each line of cmdlists into list cmdlist
cmdprocess = []
cmdreg = [0,0,0,0] #initialize list cmdreg that will be used as registers.
cmdcounter = 0 #Counter for the lines as we iterate through the commands, so we can jump around as needed.
# print(cmdlists) #Testing for what is stored in cmdlists
cmdn = len(cmdlists)

while cmdcounter < cmdn:
    cmdprocess = cmdlists[cmdcounter] #This picks one line for iteration through the program in sequence.
    cmdprocess = cmdprocess.rstrip("\n") #removes the newline command from each line.
    cmdprocess = cmdprocess.split() #splits the process into its own list for processing.
    for i in range(len(cmdprocess)): #This will transform all numbers in the string into integers.
         if i == 0: 
              continue #We actively ignore the first item on the list, as that is our command.
         else:
              cmdprocess[i] = int(float(cmdprocess[i])) #Converts everything that isn't the first item into an integer.
    # print(cmdprocess) #Testing to see output of cmdprocess.
    if cmdprocess[0] == "ADD": #Our add function
        cmdsum =  cmdreg[cmdprocess[1]] + cmdreg[cmdprocess[2]]
        cmdreg[cmdprocess[3]]=cmdsum #sets register X from the Add command to the sum value returned by the command.
        cmdcounter += 1
    elif cmdprocess[0] == "SET": #Our set function 
        cmdreg[cmdprocess[2]]=cmdprocess[1] #Sets a number into a defined register
        cmdcounter += 1
    elif cmdprocess[0] == "PRT": #Our print function
            cmdprint = cmdreg[cmdprocess[1]] #sets variable cmdprint to the called register value.
            print(f"{cmdprint}") #prints the contents of cmdprint
            cmdcounter += 1
    elif cmdprocess[0] == "GLT": #our go to line function
        if cmdreg[cmdprocess[1]] < cmdreg[cmdprocess[2]]: #If register x is less than register y, go to line z
            cmdcounter = cmdprocess[3] #sets our line counter equal to z
        else:
            break
    elif cmdprocess[0] == "END": #Our end function
            break

#ADD

#SET

#PRT

#GLT

#END
