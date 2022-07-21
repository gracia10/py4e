n1 = 1
n2 = 1.5
str = 'Hello'

print(type(n1))  # <class 'int'>
print(type(n2))  # <class 'float'>
print(type(str)) # <class 'str'>

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
n1 + str

# ValueError: invalid literal for int() with base 10: 'Hello'
int(str)
