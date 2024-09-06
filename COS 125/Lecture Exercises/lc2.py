x = 0
y = 0
print(id(x), id(y))

#Start
#Stop
#Step

r1 = range(0,9,3)

#while loop

i = 0

while 1 < 10:
    print(i)
    i+=1 #same as i = i + 1

for k in range(10):
    print(k)

def addTwoPositive(numOne, numTwo):
    c = numOne + numTwo
    if c < 0:
        c = 0
    return c