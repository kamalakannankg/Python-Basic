"""
    text type     - str
    numeric type  - int,float,complex
    sequence type - list,tuple,range
    mapping type  - dict
    set type      - set,frozenset
    boolean type  - bool
    binary type   - bytes,bytearray,memoryview
    none type     - NoneType
"""
x=5
print(type(x))

x="hi"
print(type(x))

x=20
print(type(x))

x=2.5
print(type(x))

x=1j
print(type(x))

x=["A", "B", "c"]
print(type(x))

x=("A", "B", "c")
print(type(x))

x=range(8)
print(list(x))

x={"name" : "stark", "age" : 26}
print(type(x))

x={"name", "stark", "age"}
print(type(x))


x=frozenset({"apple", "orange", "cherry"})
print(type(x))

x=True
print(type(x))

x=b"hi"
print(type(x))

x=bytearray(5)
print(type(x))

x=memoryview(bytes(5))
print(type(x))