'''
Logan McLaughlin
Lab 10
'''

#Task 1

# def BaseConvert(x):
#     returnBaseVals = []
#     returnBaseVals.append(bin(x))
#     returnBaseVals.append(hex(x))
#     return returnBaseVals

# task1 = int(input("Task 1 Test: Please insert an integer value of Base 10"))
# taskReturn = BaseConvert(task1)
# print(f"Binary value: {taskReturn[0]}\n Hexadecimal value: {taskReturn[1]}")

#Task 2
import random

def ComboMax():
    genCount = 0
    countNum = []
    sumTotal = 100
    sum = 0
    sumStart = 0
    sumCount = 0
    comboVal = []
    comboMaxVals = []
    while genCount < 11: #Random Number Generator. Will generate 10 numbers.
        randomGet = random.randint(1,50)
        countNum.append(randomGet)
        genCount += 1
    print(countNum) #Will return values generated from RNG.
    while sumStart < len(countNum): #While the start counter is less than the total values in our RNG list:
        while sumCount < len(countNum): #While our counter is less than the total values in our RNG list:
            while sum < sumTotal: #While our sum is less than our maximum allowed limit:
                sum += countNum[sumCount] #Adds the value of our RNG list from the counter of values.
                if sum > sumTotal: #If that pushes it over our limit...
                    sum = sum - countNum[sumCount] #Reverses the last addition.
                    sumCount += 1 #goes to the next iteration.
                    if sumCount > len(countNum): #If our counter goes out of the range of our RNG values...
                        comboVal.append(countNum[sumCount-1]) #Appends the Combo Val with the last value added.
                        comboMaxVals.append(comboVal) #Appends our master list with this list.
                        sumStart += 1
                        sumCount = sumStart
                if sum == sumTotal:
                    comboVal.append(countNum[sumCount])
                    comboMaxVals.append(comboVal)


                
#Class ended before I could finish this task. Hopefully you can see what I was trying to do!



ComboMax()