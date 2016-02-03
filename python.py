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
worth = 1000.0


# Python is strongly typed. Variables have to be cast after being set.
assert 'I am worth ${}'.format(worth) == 'I am worth $1000.0'


a = 'hello world'  # Immutable strings
b = "single or double quotes can be used for string literals."

# slice operator, [start:stop:step]
assert a[0:4] == 'hell'
assert a[:4] == 'hell'
assert a[1::2] == 'el ol'

c = 1
d = 3
# indentation determines scope for control structures, etc.
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
    c += 1

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


# -----------------------------------------------------------------------------
# -- Functions
# -----------------------------------------------------------------------------

# keyword def introduces function definition.
# Python functions can return multiple values
def mult(i, j):
    return i * j, '!'


result, exclamation = mult(2, 3)
print result
print exclamation


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

# return a copy of the string with its first character capitalized
# and the rest lowercased
assert my_string.capitalize() == 'Hello world'

# return centered in a string of length 'width'
assert my_string.center(20) == '    hello world     '

# return number of non-overlapping occurrences of substring
assert my_string.count('l') == 3

# return True if string ends with specified suffix, otherwise return False
assert my_string.endswith('world') is True

# return the lowest index in the string where substring is found
assert my_string.find('lo') == 3

# return true if all characters in the string are alphanumeric and
# there is at least one character, false otherwise
assert my_string.isalnum() is False

# return true if all characters in the string are alphabetic and
# there is at least one character, false otherwise
assert my_string.isalpha() is False

# return true if all characters in the string are digits and
# there is at least one character, false otherwise
assert my_string.isdigit() is False

# return true if all cased characters [4] in the string are lowercase and
# there is at least one cased character, false otherwise
assert my_string.islower() is True

# return true if there are only whitespace characters in the string and
# there is at least one character, false otherwise
assert my_string.isspace() is False

# return true if the string is a titlecased string and there is at
# least one character, false otherwise
assert my_string.istitle() is False

# return true if all cased characters in the string are uppercase and there
# is at least one cased character, false otherwise
assert my_string.isupper() is False

# return the string left justified in a string of a given length
assert my_string.ljust(20) == 'hello world         '

# return a copy of the string converted to lowercase
assert my_string.lower() == 'hello world'

# return a copy of the string with leading characters removed
assert my_string.lstrip('eh') == 'llo world'

# return a copy of the string with all occurrences of substring replaced
assert my_string.replace('l', 'Z') == 'heZZo worZd'

# return the highest index in the string where substring is found
assert my_string.rfind('o') == 7

# return the string right justified in a string of a given length
assert my_string.rjust(20) == '         hello world'

# return a copy of the string with trailing characters removed
assert my_string.rstrip('dlr') == 'hello wo'

# return a list of the words in the string
# default delimiter = consecutive whitespace
assert my_string.split() == ['hello', 'world']
assert 'hello      world'.split() == ['hello', 'world']

# return True if string starts with the prefix, otherwise return False
# prefix can also be a tuple of prefixes to look for
assert my_string.startswith('hel') is True
assert my_string.startswith(('ab', 'cd', 'hel')) is True

# Return a copy of the string with the leading and trailing characters removed
assert '   test string   '.strip() == 'test string'
assert my_string.strip('hled') == 'o wor'

# return a copy of the string with uppercase characters converted to
# lowercase and vice versa
assert 'hElLo WoRlD'.swapcase() == 'HeLlO wOrLd'

# Return a titlecased version of the string where words start with an
# uppercase character and the remaining characters are lowercase
assert my_string.title() == 'Hello World'

# return a copy of the string converted to uppercase
assert my_string.upper() == 'HELLO WORLD'

# Return a copy of the string left filled with ASCII '0' digits to
# make a string of a given length
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
# -- Tuples
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

# single value Tuple
p = 'z',
q = tuple('z')
assert p == q == ('z',)


# -----------------------------------------------------------------------------
# -- Sets
# -----------------------------------------------------------------------------

my_set = {4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1}
my_set_2 = {7, 7, 6, 6, 5, 5, 4, 4, 4}
assert my_set == {1, 2, 3, 4} == {4, 1, 3, 2}
assert my_set_2 == {4, 5, 6, 7} == {6, 5, 7, 4}

# add a value to the set
my_set.add(5)
assert my_set == {1, 2, 3, 4, 5}

# return a new set with a shallow copy of 'r', assigned to the value, 't'
copy_of_set = my_set.copy()
assert copy_of_set == my_set

# clear all contents inside the set
copy_of_set.clear()
assert copy_of_set == set([])

# return a new set with elements that are not in the other set(s)
assert my_set.difference(my_set_2) == {1, 2, 3}
assert my_set_2.difference(my_set) == {6, 7}

# remove a value from the set
my_set.remove(1)
assert my_set == {2, 3, 4, 5}


# -----------------------------------------------------------------------------
# -- Classes
# -----------------------------------------------------------------------------

# Python is object oriented
# super class is in parenthesis
class FileInfo(UserDict):
    """ doc string documents the class """

    # __init__ is constructor
    def __init__(self, fileName=None):
        """ function doc string """
        pass


# -----------------------------------------------------------------------------
# -- Comprehensions
# -----------------------------------------------------------------------------

# dict, list, set, tuple...
