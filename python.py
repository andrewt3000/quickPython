# Inspired by Learn Lua in 15 mintues http://tylerneylon.com/a/learn-lua/
# pound character starts a one line comment.
'''
    triple quotes start a multi line string.
    This also serves as a comment, and a doc string.
'''

#import modules
# this method requires fully typing namespace.
import sys
# this method lets you use the class without typing for namespace.
from UserDict import UserDict

# 1 variables and control flow

# Everything in Python is an object.
# Python is dynamically typed. (You don't declare type)
# An integer assignment
counter = 100
# A floating point
worth   = 1000.0

#Python is strongly typed.  variables have to be cast after being set.
print "I am worth $" + str(worth)

a = "hello world" #Immutable strings
b = 'single or double quotes can be used for string literals.'

#splice operator, prints hell
print a[0:4]


a = 1
b = 3
#indentation determines scope for control structures, etc.
if a==1 and b!=1 :
	print "a is one"
	print "this is also printed conditionally."

elif a != 1 :
	print "this will not print"
	print "this will also not print."
else:
    print 'winter is coming'

#while loop
while a <= 3:
    print a
    a += 1 #no ++ increment operator

#for loop. prints 1 2 3
for i in [1, 2, 3]:
    print i

print 'prints range: 0, 1, 2'
for i in range(0,3):
	print i 

# ** raises to a power. prints 9
x = 3 ** 2
print x

# The "null" value in python is represented by keyword None.
# is keyword is identity operator
x = None
if x is None :
    print "x is None."

#logic operators don't return a boolean.
#they return the values they compare
#this prints: b
print "a" and "b"

#0, '', [], (), {}, and None evaluate to false
print '' and 'b'  #print a blank.

if '' and 'b':
    print 'this will not print'

# keyword def introduces function definition.
# python functions can return multiple values
def mult(x, y):
    z = x * y
    return z, '!'

myZ, xclaim = mult(2, 3)
print myZ
print xclaim

#Python doesn't have a traditional main method, it just runs the script
#This is the standard way to invoke the main method.
def main():
    print "main method"

if __name__ == '__main__':
    main()

# Python data structures:
# The dictionary, like json.
dict = {"attribute1": "value1", "attribute2": "value2"}

#The list.
li = ['a', 'b', 'c', 1]
print li

# A tuple is an immutable list
t = ("a", "b", "c")

#Python is object oriented
#super class is in parenthesis
class FileInfo(UserDict):
    'doc string documents the class'
    #__init__ is constructor
    def __init__(Self, fileName = None):
        'function doc string'
        return None

print 'this is the end'
