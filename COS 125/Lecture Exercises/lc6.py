def LinearSearch(alist, item):
    for i in rance(len(alist)):
        if alist[i] == item:
            return i
    return None

def BinarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    mid = (right+left) // 2

    while left <= right:
        if item==alist[mid]:
            return mid
        elif item < alist[mid]:
            print(f"leeft: {item} < {alist[mid]}")
            right = mid-1
        elif item > alist[mid]:
            print(f"Right: {item} > {alist[mid]}")
            left = mid+1
        mid = (right+left)//2
    return None

def JumpSearch(alist, item):
    index = 0
    jmp = int(len(alist)**0.5) #Take sqrt of element of list
    print(f"Jump = {jmp}")
    while index < len(alist): #While not at the end of the list
        if item == alist[index]: #If at the correct index
            return index #return index
        elif item > alist[index]: #If it's not correct, jump forward.
            print(f"{item} < {alist[index]}. Indes {index}")
            index += jmp
        elif item < alist[index]: #If it's not correct, jump backward.
            print(f"{item} > {alist[index]}. Index {index}")
            index -= jmp
            jmp = 1
    return None

def mainJump():

    ele = 1000

    L = []
    for i in