# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)


>>> True
>>> False
>>> False


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

>>> b is not greater than a

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

>>> True
>>> True

# functions that returns a Boolean Value

def myFunction() :
  return True

print(myFunction())

>>> True

def myFunction():
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

>>> YES!

x = 200
print(isinstance(x, int)) # used to determine if an object is of a certain DT

>>> True
