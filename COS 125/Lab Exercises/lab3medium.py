'''Logan McLaughlin
Lab 3: Loops
Task 2: Medium Difficulty'''

L = ["A", "B", "C", "D", "E"]
for x in range(11):
    y = 0
    for y in range(6):
        print(f"For Loop counter: Inner {y} of 5, outer {x} of 10")

whileX = 0
whileY = 0
while whileX <= 4:
    whileY = 0
    while whileY <= 8:
        print(f"While Loop counter: Inner {whileY} of 8, outer {whileX} of 4")
        whileY += 1
    whileX += 1

i = 0
while i < 5:
    print(L[i])
    i += 1

for L in L:
    print(L)