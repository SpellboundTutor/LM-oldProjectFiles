#Logan McLaughlin
#COS 125 Lab 2
#September 21, 2023

#Task 2 - if-elif-else Blocks

x = float(input("Please define x for the first if-block."))
if x > 1:
    x = 1
elif x < -1:
    x = -1
else:
    x = 0
print(f"x = {x}")

y = float(input("Please define y for the second if-block."))
if y>10 and y<20:
    print("Yes")
else:
    print("No")

a = float(input("Please define a for the third if-block."))
b = float(input("Please define b for the third if-block."))
c = float(input("Please define c for the third if-block."))

if a == b or a == c:
    print("Correct")
else:
    print("Incorrect")

t = float(input("Please define t for the fourth if-block."))
if t == int(t):
    t = int(t)
print(t)