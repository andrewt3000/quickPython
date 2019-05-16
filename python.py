# Inspired by Learn Lua in 15 minutes http://tylerneylon.com/a/learn-lua/

# -----------------------------------------------------------------------------
# Python 2 - Documentation: https://docs.python.org/2/
# Python 3 - Documentation: https://docs.python.org/3/
# Python PEP8 - Style Guide: https://www.python.org/dev/peps/pep-0008/
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# -- Comments
# -----------------------------------------------------------------------------

# pound character starts a one line comment.

"""
    triple quotes start a multi line string.
    This also serves as a comment, and a doc string.
"""


# -----------------------------------------------------------------------------
# -- Imports
# -----------------------------------------------------------------------------

# import modules
# this method requires fully typing namespace.
import sys
# this method lets you use the class without typing for namespace.
from UserDict import UserDict


# -----------------------------------------------------------------------------
# -- Variables and Control Flow
# -----------------------------------------------------------------------------

# Everything in Python is an object.
# Python is dynamically typed. (You don't declare type)

# An integer assignment
counter = 100

# A floating point
worth = 999.56

# Python is strongly typed. Variables have to be cast after being set.
assert 'I am worth ${:.0f}'.format(worth) == 'I am worth $1000'
print "worth " + str(worth) #int(), float()


a = 'hello world'  # Immutable strings
b = "single or double quotes can be used for string literals."

# slice operator, [start:stop:step] 
# slice is used to substring or get ranges for list.
assert a[0:4] == 'hell'
assert a[:4] == 'hell'
#gets even indexes
assert a[1::2] == 'el ol'

c = 1
d = 3
# indentation determines scope for control structures, etc.
# python supports "and", and "or" keywords for boolean logic. also support short circuiting.  
if c == 1 and d != 1:
    print 'c is one'
    print 'this is also printed conditionally.'
elif c != 1:
    print 'this will not print'
    print 'this will also not print.'
else:
    print 'winter is coming'

# while loop
while c <= 3:
    print c
    c += 1  # no ++ increment operator

# for loop. prints 1 2 3
for e in [1, 2, 3]:
    print e

print 'prints range: 0, 1, 2'
for f in range(0, 3):
    print f

# ** raises to a power. prints 9
assert 3 ** 2 == 9

# The 'null' value in Python is represented by keyword None
# 'is' keyword is identity operator
h = None
if h is None:
    print 'h is None'

# logic operators don't return a boolean.
# they return the values they compare
# this prints: b
print 'a' and 'b'

# 0, '', [], (), {}, and None evaluate to false
print '' and 'b'  # print a blank.

if '' and 'b':
    print 'this will not print'

#not is the negation operator
if not false
    print 'this will print'

# -----------------------------------------------------------------------------
# -- Functions
# -----------------------------------------------------------------------------

# keyword def introduces function definition.
# Python functions can return multiple values
def mult(i, j):
    return i * j, '!'


result, exclamation = mult(2, 3)
assert result == 6
assert exclamation == '!'


# Python doesn't have a traditional main method, it just runs the script
# This is the standard way to invoke the main method.
def main():
    print 'main method'


if __name__ == '__main__':
    main()


# -----------------------------------------------------------------------------
# -- Strings
# -----------------------------------------------------------------------------

my_string = 'hello world'

#sub string is accomplished with range operator
#if a string contains a sub string can be accomplished with in operator.
assert my_string.capitalize() == 'Hello world'
assert my_string.center(20) == '    hello world     '
assert my_string.count('l') == 3
assert my_string.endswith('world') is True
assert my_string.find('lo') == 3
assert 'My name is {}'.format('Guido') == 'My name is Guido'
assert 'abc123'.isalnum() is True
assert 'abc'.isalpha() is True
assert '123456'.isdigit() is True
assert 'abc'.islower() is True
assert '  '.isspace() is True
assert 'Hello World'.istitle() is True
assert 'HELLO WORLD'.isupper() is True
assert ' '.join(['hello', 'world']) == 'hello world'
assert my_string.ljust(20) == 'hello world         '
assert 'Hello World'.lower() == 'hello world'
assert my_string.lstrip('eh') == 'llo world'
assert my_string.replace('l', 'Z') == 'heZZo worZd'
assert my_string.rfind('o') == 7
assert my_string.rjust(20) == '         hello world'
assert my_string.rstrip('drl') == 'hello wo'
assert my_string.split() == ['hello', 'world']
assert 'hello      world'.split() == ['hello', 'world']
assert 'hello<>world<>!'.split('<>') == ['hello', 'world', '!']
assert my_string.startswith('hel') is True
assert my_string.startswith(('ab', 'cd', 'hel')) is True
assert '   test string   '.strip() == 'test string'
assert my_string.strip('hled') == 'o wor'
assert 'hElLo WoRlD'.swapcase() == 'HeLlO wOrLd'
assert my_string.title() == 'Hello World'
assert my_string.upper() == 'HELLO WORLD'
assert '2'.zfill(4) == '0002'


# -----------------------------------------------------------------------------
# -- Dict
# -----------------------------------------------------------------------------

my_dict = {'key1': 'value1', 'key2': 'value2'}

# return the item of my_dict with key -> 'key1'
assert my_dict['key1'] == 'value1'

# return the value for key if key is in the dictionary, else default
# if default is not given, it defaults to None
assert my_dict.get('key47', 'key not found!') == 'key not found!'

# test 'key1' for membership in my_dict
assert 'key1' in my_dict

# test 'abc' for non-membership in my_dict
assert 'abc' not in my_dict

# number of items in my_dict
assert len(my_dict) == 2

# delete a key/value pair from my_dict, confirm
del my_dict['key1']
assert 'key1' not in my_dict


# -----------------------------------------------------------------------------
# -- Lists
# -----------------------------------------------------------------------------

my_list = ['a', 'b', 'c', 1]
assert list('abc') == ['a', 'b', 'c']

# append to the end of the list
my_list.append('last')
assert my_list == ['a', 'b', 'c', 1, 'last']

# count total occurrences of a value in a list
assert my_list.count('a') == 1

# extend the list
my_list.extend([5, 6, 7, 8])
assert my_list == ['a', 'b', 'c', 1, 'last', 5, 6, 7, 8]

# index of a value in the list
assert my_list.index('c') == 2

# insert a value into the list, insert(index, value)
my_list.insert(4, 'd')
assert my_list == ['a', 'b', 'c', 1, 'd', 'last', 5, 6, 7, 8]

# length of the list
assert len(my_list) == 10

# pop removes the last object by default, can be saved to variable
my_tuple = my_list.pop()
assert my_tuple == 8
assert my_list == ['a', 'b', 'c', 1, 'd', 'last', 5, 6, 7]

# pop can also remove an object by index
assert my_list.pop(5) == 'last'
assert my_list == ['a', 'b', 'c', 1, 'd', 5, 6, 7]

# remove a value from the list
my_list.remove(1)
assert my_list == ['a', 'b', 'c', 'd', 5, 6, 7]

# reverse the list in-place
my_list.reverse()
assert my_list == [7, 6, 5, 'd', 'c', 'b', 'a']

# create a new sorted list
assert sorted(my_list) == [5, 6, 7, 'a', 'b', 'c', 'd']
assert sorted(my_list, reverse=True) == ['d', 'c', 'b', 'a', 7, 6, 5]
assert sorted(['aaa', 'bb', 'c'], key=len) == ['c', 'bb', 'aaa']

# original list remains the same
assert my_list == [7, 6, 5, 'd', 'c', 'b', 'a']

# sort original list in-place
my_list.sort()
assert my_list == [5, 6, 7, 'a', 'b', 'c', 'd']


# -----------------------------------------------------------------------------
# -- Tuples an immutable list
# -----------------------------------------------------------------------------

my_tuple = ('a', 'b', 'c')  # parenthesis are optional
my_tuple_2 = 'a', 'b', 'c'
my_tuple_3 = tuple('abc')
# all three variations create an equivalent tuple
assert my_tuple == my_tuple_2 == my_tuple_3

# count the total occurrences of a value in the tuple
assert my_tuple.count('c') == 1

# index of a value in the tuple
assert my_tuple.index('b') == 1

# slicing
assert my_tuple_2[1:] == my_tuple_3[-2:] == ('b', 'c')

# single value tuple
p = 'z',
q = tuple('z')
assert p == q == ('z',)


# -----------------------------------------------------------------------------
# -- Sets
# -----------------------------------------------------------------------------

my_set = {4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1}
assert my_set == {1, 2, 3, 4} == {4, 1, 3, 2}

my_set_2 = {7, 7, 6, 6, 5, 5, 4, 4, 4}
assert my_set_2 == {4, 5, 6, 7} == {6, 5, 7, 4}

# add a value to the set
my_set.add(5)
assert my_set == {1, 2, 3, 4, 5}

# return a new set with a shallow copy of the set
copy_of_set = my_set.copy()
assert copy_of_set == my_set

# clear all contents inside the set
copy_of_set.clear()
assert copy_of_set == set([])

# return a new set with elements that are not in the other set(s)
assert my_set.difference(my_set_2) == {1, 2, 3}
assert my_set - my_set_2 == {1, 2, 3}

# return a new set with elements common to the set and all others
assert my_set.intersection(my_set_2) == {4, 5}
assert my_set & my_set_2 == {4, 5}

# number of elements in the set
assert len(my_set) == 5

# test for membership
assert 2 in my_set

# test for non-membership
assert 47 not in my_set

# remove a value from the set
my_set.remove(1)
assert my_set == {2, 3, 4, 5}

# return a new set with elements in either the set or other but not both
assert my_set.symmetric_difference(my_set_2) == {2, 3, 6, 7}
assert my_set ^ my_set_2 == {2, 3, 6, 7}

# return a new set with elements from the set and all others
assert my_set.union(my_set_2) == {2, 3, 4, 5, 6, 7}
assert my_set | my_set_2 == {2, 3, 4, 5, 6, 7}


# -----------------------------------------------------------------------------
# -- Classes
# -----------------------------------------------------------------------------

# Python is object oriented
class MyClass:
    #attributes
    i = 1234
    
#Class instantiation
x = MyClass()

# super class is in parenthesis. allows multiple base classes.
class FileInfo(UserDict):
    """ doc string documents the class """

    # __init__ is constructor
    def __init__(self, fileName=None):
        """ function doc string """
        pass

#self is a keyword to reference class variables and methods. similar to "this" in other languages.  

# -----------------------------------------------------------------------------
# -- Comprehensions
# -----------------------------------------------------------------------------

# dict, list, set, tuple...
