'''
Logan McLaughlin
Lab 7
'''

def Task0():
    num = range(101,3,-1)
    for i in num:
        if i > 3:
            print(i-1)
            i -= 1

def Task1():
    S = "Most good programmers do programming not because they expect " \
"to get paid or get adulation by the public, but because it is " \
"fun to program."
    
    L = [4, 6, 2, 4, 1, 87, 4, 6, 13, 15, 99, 3]

    sWords = S.split(" ")
    for i in range(len(sWords)):
        if sWords[i] == "expect":
            print(f"{sWords[i]}\n")
            i += 1
        elif sWords[i] == "is":
            print(f"{sWords[i]}\n")
            i += 1
        elif sWords[i] == "program.":
            print(f"{sWords[i]}")
            i += 1
        else:
            print(f"{sWords[i]}_", end="")
            i += 1
