from lab5_code import *

############################################################
# INSTRUCTIONS
# Read each function specification below and write tests
# to find any errors in the function. An error is any
# behavior contrary to the specification. Every function
# has at least one error.

# But DO NOT read the lab9_code.py file. Your job is to
# find the errors through testing, not by reading the
# function code.

# At the end of the lab we will talk through the errors
# in each function.

# Write your tests in the space indicated beneath each
# specification.


############################################################
# Name: DivideOnLessThan
# Header: def DivideOnLessThan(a,b)
# Parameters:
#   a: int or float
#   b: int or float
# Return:
#   float
# Description: This function has two parameters: a and b.
#   This function returns a/b if b < a. If b > a, then it
#   return 0.0

# WRITE TESTS HERE

a = 10
b = 5
test1 = DivideOnLessThan(a,b)
print(f'a>b (DivideOnLessThan) result: {test1}')

a = 5
b = 6
test1 = DivideOnLessThan(a,b)
print(f'a<b (DivideOnLessThan) result: {test1}')

a = 6
b = 6
test1 = DivideOnLessThan(a,b)
print(f'a=b (DivideOnLessThan) result: {test1}')

############################################################
# Name: AskYesOrNo
# Header: def AskYesOrNo():
# Parameters:
#   None
# Return:
#   Returns True if the user types any variant of yes or y
#   Returns False if the user types any variant of no or n
# Description:
#   Asks for yes or no repeatedly until the user gives an
#   accepted answer. Ignores case.

# WRITE TESTS HERE


test2 = AskYesOrNo()
print(f'AskYesOrNo Test result: {test2}')



############################################################
# Name: SearchListInReverse
# Header: def SearchListInReverse(alist, item)
# Parameters:
#   alist: a list
#   item: element to search for
# Return:
#   If item is in the list, returns index of item. 
#   If the item is not found in the list, None is returned.
# Description: This function searches through the list alist
#   for the element stored in item.

# WRITE TESTS HERE

alist = [1,2,3,"a","b","c"]
item = "a"
test3 = SearchListInReverse(alist, item)
print(f"SearchListInReverse Successful Test Result: {test3}")

item = [0]
test3 = SearchListInReverse(alist, item)
print(f"SearchListInReverse Unuccessful Test Result: {test3}")

############################################################
# Name: SplitStringAtPunctuation
# Header: def SplitStringAtPunctuation(astring)
# Parameters:
#   astring: a string that might or might not have punctuation.
# Return:
#   Returns a list containing the split strings with the punctuation
#   removed.
# Description: This function splits a string at punctuation.
#   Punctuation includes: . ? !
#   It does not remove whitespace before or after the splits.

# WRITE TESTS HERE

astring = "A string with Punctuation. Will this split the string at the punctuation marks? Let's find out! Execute the function."
test4 = SplitStringAtPunctuation(astring)
print(f"Test 4: SplitStringAtPunctuation Results 1: {test4}")

astring = "This is a sentence with only punctuation at the end."
test4 = SplitStringAtPunctuation(astring)
print(f"Test 4: SplitStringAtPunctuation Results 1: {test4}")

astring = "this is a string written without punctuation because we need to test a string that doesn't have punctuation to make sure it works"
test4 = SplitStringAtPunctuation(astring)
print(f"Test 4: SplitStringAtPunctuation Results 2: {test4}")


############################################################
# Name: ChoiceDiscrete
# Header: def ChoiceDiscrete(alist, problist):
# Parameters:
#   alist: a list of any type.
#   problist: a list of probabilities (ints or float). 
#       Must be the same size as alist.
# Return:
#   Returns a random element from alist. 
# Description: The probability
#   of each element being returned is given by the
#   problist. For example, if alist has two elements and
#   problist contains [1,8], then the second element in
#   alist is 8 times more likely to be returned than
#   the first element. In other words, probabilities are
#   relative.

# WRITE TESTS HERE

alist = [1,3,5,6,7,10,15]
problist = [8,6,7,5,3,1,9]
test5 = ChoiceDiscrete(alist, problist)
print(f"Test 5: ChoiceDiscrete results: {test5}")