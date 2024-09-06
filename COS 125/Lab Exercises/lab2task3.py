#Logan McLaughlin
#COS 125 Lab 2
#September 21, 2023

#Task 3 - While Loops

taskOne = 1
while taskOne <11:
    print(taskOne)
    taskOne += 1

taskTwo = 10
while taskTwo >0:
    print(taskTwo)
    taskTwo -= 1

taskThree = input("Please type a lowercase q.")
while taskThree != "q":
    print("Sorry, please try again.")
    taskThree = input("Please type a lowercase q.")

taskFour = input("Do you wish to start a [n]ew game, [l]oad a saved game, or [q]uit?")
while taskFour == "q" or "Q":
    print("Quitting game. Thank you for playing!")
while taskFour == "n" or "N":
        print("Starting new game...")
        taskFour = input("Do you wish to start a [n]ew game, [l]oad a saved game, or [q]uit?")
while taskFour == "l" or "L":
        print("Loading new game...")
        taskFour = input("Do you wish to start a [n]ew game, [l]oad a saved game, or [q]uit?")
taskFour = input("Do you wish to start a [n]ew game, [l]oad a saved game, or [q]uit?")
    

taskFive = range(1,1000,2)
taskFiveSum = 0
while taskFive <1000:
    taskFiveSum += taskFive
print(taskFiveSum)