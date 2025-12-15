#Strings
"""Strings in python are surrounded by either 
single quotation marks, or double quotation marks."""

print("Hello")
print('hi')

#Inside Quotes
print("It's okey restart")
print("hi 'everyone'")
print('hi "everyone"')

#Assign string to a variable
a="hi"
print(a)

#Multiline strings
a="""Work hard in silence,
let success make the noise"""
print(a)

b='''Don't watch the clock; 
do what it does,keep going'''
print(b)

#Note: in the result, the line breaks are inserted at the same position as in the code.


#Strings are Arrays
"""  strings in Python are arrays of unicode characters.

Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""

x="hi everyone"
print(x[6])

#Looping through a strings
"""strings are arrays, we can 
loop through the characters in a string, with a for loop."""

for a in "everyone":
    print(a)

#string length
'''To get the length of a string, use the len() function.'''

x="everyone"
print(len(x))

#Check string
'''To check if a certain phrase or character is present in a string,
we can use the keyword 'in'.'''

"""Check if "free" is present in the following text:"""

txt="The best things in life are free!"
print("free" in txt)

"""if statement"""
txt="The best things in life are free!"
if 'free' in txt:
    print("yes, 'free' is present.")

"""if NOT statement"""
txt="The best things in life are free!"
print("expensive" not in txt)    

"""if statement"""
txt="The best things in life are free!"
if "expensive" not in txt:
    print("no,'expensive' is NOT present.")
    
"""....................................................................."""

#Slicing
'''you can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon,
to return a part of the string.'''

"""Get the characters from position 2 to position 5 (not included):"""

a="hello, world!"
print(a[2:8])

#Slice from start
'''Get the characters from the start to position 5 (not included):'''
a="hello, everyone"
print(a[:7])

#slice to the end
'''Get the characters from position 2, and all the way to the end:'''
b="hello, good morning"
print(b[3:])

#Negative indexing
"""negative indexes to start the slice from the end of the string:"""

x="hello, world!"
print(x[-10:-2])

"""....................................................................."""

#Modify strings

#Upper case
a="hi everyone"
print(a.upper())

#Lower case
a="HI HELLow"
print(a.lower())

#Remove whitespace
"""The strip() method removes any whitespace from the beginning or the end:"""
a=" hi and hello "
print(a.strip())

#Replace string
x="holy day"
print(x.replace("h","J"))

#split string
a="hi,everyone"
print(a.split(","))

"""....................................................................."""

#concatenation
"""To concatenate, or combine, two strings you can use the + operator."""
a="hi"
b='everyone'
c=a + b
print(c)

#add space between them

a="hi"
b='everyone'
c=a + " " + b
print(c)

"""....................................................................."""

#Format string
'''we learned in the Python Variables
chapter, we cannot combine strings and numbers'''

"""can combine strings and numbers by 
using f-strings or the format() method!"""

#f-strings

'''To specify a string as an f-string, simply put 
an f in front of the string literal, and 
add curly brackets {} as placeholders for variables and other operations.'''

age= 25
txt=f"my name is jack, I am {age}"
print(txt)

#placeholders and modifiers

"""A placeholder can contain variables, operations,
functions, and modifiers to format the value."""

price=65
txt=f"the price is {price} dollars"
print(txt)

'''A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a
legal formatting type, like .2f which means fixed point number
with 2 decimals:'''

price=23
txt=f"the price is {price:.2f} dollars"
print(txt)

'''A placeholder can contain Python code, like math operations:'''
txt=f"the price is {20*5} dollars"
print(txt)