'''Logan McLaughlin
Lab 9'''

#Task 1

def Task1():
    v = 'Something "Complex".' #3 lines feels insufficient to do anything. So I'll just be cheeky.
    print(v)

#Task 2

def FuncA(A, B):
    C = []
    for a in A:
        for i in range((len(B))-1, -1, -1):
            C.append(a+B[i])
    return C
    
list1 = [1,2,3]
list2 = [10,100]
list3 = [FuncA(list1, list2)]

#The first thing I got was a syntax error because there was one parenthesis missing.
#When that error was fixed, I got a second error, saying "FunA" is not defined.
#The third thing I got when both of those were fixed was the path of my Python executable, then the path of this assignment.

#Task3
#Copied the program line by line here, commented.

# def Parse(line): #Defines the program
#     data = [] #Defines var 'data' as a list
#     start = 0 #Defines var 'start' as int with val of 0
#     end = 0 #Defines var 'end' as int with val of 0
#     while end < len(line): #While loop to see if the number of values (N) of the imported line is greater than end.
#         if line[end] = ":": #If line at point 'end' is a colon...
#             if line[start:end]: #If line is starting at start and ending at end??
#                 data.append(line[start:end]) #appends line with the information starting at start and ending at end.
#             end += 1 #adds 1 to the end variable. Counter.
#             start = end #Sets start to end.
#         else:
#             end += 1 #If there is no colon where line is, add 1 to end variable.
#     if end > start: #If the end variable is greater than the start variable...
#         data.append(line[start:]) #Data is appended to the end of the line at point start within the imported data.
#     return data

#Going through each line, I assume we're just slicing a string by colons? But some bits are confusing. Will try to clean it up.

def Parse(line):
    data = [] #Definining this as a list is fine. No problems here.
    data = line.split(sep=":") #There's a built-in function for that. :)
    return data

#This should be a fair bit cleaner, shorter, and more efficient.

#Task4

##Snippet 1
#This will print 2. (5 or 1) is true, which is 1, and (1 and 2) is true, which is 1. 1 + 1 = 2.

##Snippet 2
#Since we're printing the len of L, and the len of L never once changes, it's just 1.

##Snippet 3
#We start by adding the lists together, so A[1:3] would be 2,3,4, then A[1:-2] would be 2, as there's no step indicator going backwards.
#This means we're adding the lists together for B = [2,3,4,2]. If we sum that, we would get 11.

##Snippet 4
#It would loop a couple of times, c would get these values, in order: 0, 5, 2, 7, 4, 9, 6, then 10, where it would stop. It would print 10.

##Snippet 5
#First, splits the line into a list of five. Then sets variable "m" to 0.
#Next, iterates down the list. As i starts at 0, it cannot be less than m, which is 0 by default, so nothing happens to change m, which means the for loop just kinda doesn't do anything.
#The printed line would just be where 0 is, which is "e133".

