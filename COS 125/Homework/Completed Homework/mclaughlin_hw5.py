'''
Logan McLaughlin
Homework 5: Oops! All Functions!
Helps used:
'''
import random

def EleAdd(L1, L2):
    L3 = []
    x = 0
    i = 0
    if len(L2) > len(L1):
        for i in range(len(L1)):
            x = L2[i] + L1[i]
            L2[i] = x
        return(L2)
    else:
        for i in range(len(L2)):
            x = L1[i] + L2[i]
            L1[i] = x
        return(L1)

def FindSL(astr):
    t = []
    t = astr.split(' ')
    for i in range(len(t)):
        t[i] = t[i].replace('.', '')
        t[i] = t[i].replace(',', '')
        t[i] = t[i].replace('!', '')
        t[i] = t[i].replace('?', '')
        t[i] = [len(t[i]), t[i]]
        i += 1
    t.sort(reverse=True)
    mint = min(t)
    maxt = max(t)
    minmaxt = (mint[1], maxt[1])
    return(minmaxt)

def FindMedian(arr):
    if len(arr) == 0:
        return None
    elif len(arr) & 2 != 0:
        x = len(arr)
        N = float(arr[x-1])
        return (N//2)
    else:
        minarr = float(min(arr))
        maxarr = float(max(arr))
        return float((minarr+maxarr)/2)
    
def Create2DList(n, m, val):
    if n <= 0:
        return([])
    elif m <= 0:
        return([]*n)
    else:
        i = 0
        nlist = []
        for i in range(n):
            j = 0
            mlist = []
            for j in range(m):
                mlist.append(val)
                j += 1
            nlist.append(mlist)
            i += 1
        return(nlist)

def UniqueRandList(a, b, amt):
    if b < a:
        return []
    elif ((abs(b-a))+1) < amt:
        return []
    else:
        randlist = []
        counter = 0
        while counter < amt:
            randval = random.randint(a,b)
            if randval in randlist:
                continue
            else:
                randlist.append(randval)
                counter += 1
        return(randlist)

