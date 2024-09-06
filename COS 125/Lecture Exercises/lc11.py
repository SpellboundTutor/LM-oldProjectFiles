#Quiz will be on recursion! What is the base case? WTF does it do?
#HW8 due December 8; will use Classes and Objects
#This week's lab is on Recursion
#Next week's lab is on Classes and Objects
#Final is on Friday; Will not be a 2 hour final, more "Quiz++", will be an amalgamation of all prior quiz questions.

#MLA Survey posted

#Classes and Functions

'''
A function is a generalized snippet that processes input.

"If you need to simulate a rectangle, you might need to store x and y for some corner.
Let's say we're going to store every x, y for each corner.
Could be stored in a list of tuples.
If you need another rectangle? Make another list!
But this could be inefficient; not very readable. Also not growable.
We would have to pass in a list and treat it as a rectangle when it's not super obvious.

This is where objects and classes came about!

"Encapsulation"

A class is a template.

If you need to model a rectangle, you need four points. Every time we want to create from this template.
"If there is a rectangle, they have these four points."
Put only the stuff in there that will be logical.

There are no classes in C. C++ added classes and "other junk".

'''

# class Rectangle:
#     x #data members, meaning variables relating to the class.
#     y
#     w
#     h 

#Don't make a class this way!

class Person:
    def __init__(self): #initialization function. self is not an actual parameter; It's something Python uses to fill in for the object itself.
        self.name = ""
        self.age = ""
        self.height = ""
        self.occupation = ""

class Person:
    def __init__(self, name, age, height,): #initialization function. self is not an actual parameter; It's something Python uses to fill in for the object itself.
        self.name = ""
        self.age = ""
        self.height = ""
        self.occupation = ""

class Person:
    def __init__(self, name, age, height, occupation=None): #initialization function. self is not an actual parameter; It's something Python uses to fill in for the object itself.
        self.name = ""
        self.age = ""
        self.height = ""
        self.occupation = ""
#When we call a constructor of a function and use an init function. Sets the data up in the class.
#Since i have a function, it gets called, get to determine the parameters.
#When we create our object, they have values that makes sense. If code doesn't work, default values are used, so we can see which variables are having problems.

def main():
    r1 = Rectangle() #r1 is storing the object. Rectangle() is a constructor (a bit of a lie, but whatevs); call the class like a function.
    r1.x = 5 #From Rectangle class, creates object with these data members.
    r1.y = 10
    r1.w = 100
    r1.h = 200

p = r1.x
#From classes, you create objects. The class defines what they are.
#What is 'self'?
#Every time you reference a data member, you have to use 'self'!