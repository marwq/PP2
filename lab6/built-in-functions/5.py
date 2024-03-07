# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_true(t: tuple):
    return all(t)

print(all_true((True, True, True)))