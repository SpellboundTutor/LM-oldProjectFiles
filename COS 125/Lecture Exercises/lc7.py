'''
HW 7 due in 2 weeks
Has some "computer science jargon".
Read over homework over the next couple days to ask questions if need be.

Extra Credit HW due on Black Friday
Parsing through a string
Reading strings from command line
Use that to simulate movement on 2D board.
Extra Credit will be slipped into grade that most benefits.

Final is Friday Morning on Finals Week
'''

import sys

args = sys.argv #contains a list of strings that you put in when you put them in the program

# for i in range(len(args)):
#     print(args[i]) #when you don't put in any arguments, the first line is the file name.

# cmd_str = args[1]
# a = cmd_str[:2] #getting a slice of the argument
# print(a)

'''
Complexity
COS 226 at beginning of Sophomore Year "Seriously Mathy"

Asymtotic
    Want to be able to compare Solution A to Solution B
        Bubble Sort
        Pigeonhole Sort
    Boil down to theoretical level can help when you're academic.
    
Big O notation
"Omicron"
    An upper bound estimation, spatial complexity, time complexity
    Space: amt of bytes to solve problem
    Time: time it takes to solve problem
    Talk in terms of input size; how much adtl size (in space/time) required

If you pass input A through algorithm, then much larger input B through algorithm, how much more time does it take?

Big O "one side of the problem"

Also "Big Omega" and "Big Theta"

Big O as in "Upper Bound"

Come up with mathematical function that is "growth rate".
As complexity increases as input does, Big O increases at least as much.

Big Omega "Lower Bound"
Big Theta "Tight Bound" (Mean Value)

Best 
O(1) - The function is constant, regardless of input.
O(logn) - Function has diminishing returns.
'''