# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)


# Sets cannot have two items with the same value
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

>>> {'banana', 'cherry', 'apple'}

# Access Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

>>> {'banana', 'cherry', 'apple', 'orange', 'kiwi'}

# Remove Set Items
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Removing random item using pop()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# The clear() method empties the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


# Loop Sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


