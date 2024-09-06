'''Logan McLaughlin
Lab 4'''

#Task 1

def Hello(): #Task 1A
    print("Hello world")

def HelloTo(name): #Task 1B
    print(f'Hello, {name}!')

lista = [1,2,3,5,7,9,13,22,17,4,84,42,64,12]

def CountRange(alist, minimum, maximum): #Task 1C
    for alist in lista:
        if alist >= minimum and alist <= maximum:
            print(alist)

Hello()

HelloTo('Logan')
        
CountRange(0, 1, 12)

#Task 2

def AbsVal(num): #Task 2A
    if num < 0:
        num *= -1
    print(num)



def MinsToDaysHrsMins(minutes):
    hours = 0
    days = 0
    while minutes >= 60:
        while minutes >= (60*24):
            minutes -= (60*24)
            days += 1
        minutes -= 60
        hours += 1
    print(f"{days} days, {hours} hours, {minutes} minutes.")

def ConvertTemp(temp, scale):
    if scale == "C":
        newTemp = ((temp - 32)/(1.8))
        print(f"{newTemp} degrees Celsius.")
    if scale == "F":
        newTemp = ((1.8*temp) + 32)
        print(f"{newTemp} degrees Fahrenheit.")


AbsVal(-42)

MinsToDaysHrsMins(17500)

ConvertTemp(100, "F")

#Task 3

def FunctionA(numA): #Task 3A; FunctionA is actually a secondary function, reliant on FunctionC to function, returns the integer solution of numA divided by 2
    return numA // 2

def FunctionB(numB): #Function B, if the number from FunctionC is odd, it will subtract the number by 1 so it becomes even or 0 then run it through FunctionA.
    if numB % 2 == 1:
        return FunctionA(numB - 1)

def FunctionC(numC): #The primary engine of the function. If the number from main is greater than 10, it will return the integer after dividing the number by 3 and run it through FunctionB.
    if numC > 10:
        return FunctionB(numC // 3)
    else:
        return FunctionA(numC + 10) #Otherwise, it will add 10 to the number and run it through Function A.
    
def main():
    num = 27 #This is the input value that goes into FunctionC, then sorted into Function B and A.
    print(FunctionC(num)) #This prints the finished product after all functions are complete.

main()