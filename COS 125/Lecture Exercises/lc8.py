'''
Quiz 6 Wed, November 15
Searching, Sorting, Complexity

Search algorithms
    Linear
    Binary
    Jump Search
Sorting Algorithm
    Bubble Sort
    Consortium Sort
    Pigeonhole Sort
"As input goes to infinity..."; "To the limit..."

Complexity
    Ordering, smallest to largest

Homework 7 live, due Friday
EC Homework, due 24th Nov
    Will replace weakest grade (HW, Quiz, Lab, etc.)

Homework 8 due Dec 8th

Last quiz on last week of class
About recursion

Final will be cherry-picked from questions on all prior quizzes
    Final is optional, but will be beneficial.
'''


#Pigeonhole Sort
#   Based on Pigeonhole principal
# x = [5,2,4,10]
# z = []
# for i in x:
#     y = i + min(x)
#     z.append(y)
# print(z)

'''
Recursion
    Contains two values.
        1.) Base Case - The End (ex. if i == 10:)
        2.) Recursive Case - The Modifier (ex. i = i + 1)
    When writing a recursive function, write the base case first.
        This will let you know where the stopping point is.
    There are some functions that can have multiple base cases.
    Recursion can be better than loops in some situations!

    When solving a recursion problem, you only need to worry about solving one thing, not the entire problem.
'''

def CountTo10(n):
    print(n)
    if n >= 10:
        return
    else:
        CountTo10(n+1)

l = [1,2,3,4,5]

def RecSum(m):
    if len(m) ==1: #Base 1
        return m[0]
    elif len(m) ==0: #Base 2
        return 0
    else:
        return m[0]+RecSum(m[1:]) #slices out the second value and adds it to the first value
