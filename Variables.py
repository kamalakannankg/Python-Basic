x=5
X=float(3)
y='hi'
z="hello" # y and z are string
print(x)
print(X)
print(type(y), end=" ")
print(z)

# multi word variable name
"""camel case"""
myVarName="sky1" #Each word, except the first, starts with a capital letter:

'''pascal case'''
MyVarName="sky2" #Each word starts with a capital letter:

"""snake case"""
my_var_name="sky3" #Each word is separated by an underscore character:

print(myVarName, end=" "); print(MyVarName, end=" "); print(my_var_name)

x,y,z="hi", "hello", "welcome"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

veg=["betroot", "carrot", "beans"]
x,y,z=veg
print(x)
print(y)
print(z)

x="hi"
y="hello"
z="welcome"
print(x,y,z)

x="hi "
y="hello "
z="welcome"
print(x+y+z)

x=2
y=3
print(x+y)

x=5
y='hello'
print(x,y)

#Global Variables
"""Variables that are created outside of a function"""

x="stark"
def myfunc():
    print("i'm", x)
    
myfunc()

a="Hi"
def myfunc():
    a='hello'
    print(a)
myfunc()
print(a)

def myfunc():
    global x
    x="awesome"
myfunc()
print("great initiate is", x)


x='hi'
def myfunc():
    global x
    x="hello"
myfunc()
print(x)