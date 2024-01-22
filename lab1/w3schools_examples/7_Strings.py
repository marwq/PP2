long_text = """
Hello World, this is a long text
as you can see
"""

for char in long_text:
    print(char)
    
print(len(long_text))
print(long_text[10])

if 'a' in long_text:
    print('a is in long_text')
    

# Slicing string
print(long_text[0:5])
print(long_text[-5:-1])
print(long_text[0:5:2])
print(long_text[::2])
print(long_text[::-1])

# Modify string
print(long_text.upper())
print(long_text.lower())
print(long_text.strip())
print(long_text.replace('Hello', 'Hi'))
print(long_text.split(','))

# Concatenate string
print(long_text + ' ' + long_text)

# Format string
name = 'Bauyrgazy'
age = 18
height = 179.5
print('My name is {}, I am {} years old, and my height is {}'.format(name, age, height))

# Escape character
print('Hello \'World\'')

# String methods
print(long_text.capitalize())
print(long_text.casefold())

# Check string
print(long_text.isalpha())
print(long_text.isalnum())
print(long_text.isdecimal())