'''There are three numeric types in Python.
int
float
complex'''

x=1
y=6.5
z=5j
print(type(x))
print(type(y))
print(type(z))

#Int
x=12332
y=3
z=-24378
print(type(x))
print(type(y))
print(type(z))

#Float
a=5.154
b=7.1
c=-52.6
print(type(a))
print(type(b))
print(type(c))

""" Float can also be scintific numbers with an 'e' to indiacte the 
power of 10"""
x=54e6
y=45E2
z=-65.2e100
print(type(x))
print(type(y))
print(type(z))

#complex

""" complex number are writtern with a 'j' as the imaginary part"""
x=5+2j
y=8j
z=-3j
print(type(x))
print(type(y))
print(type(z))

#type convertion
'''you can convert from one type to another
with the int(), float(), and complex() methods'''
x=4
y=6.45
z=9j
a=float(x)
b=int(y)
c=complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Note:can't convert cmplex number into anoter number type

#Random number

import random
print(random.randrange(1, 10))