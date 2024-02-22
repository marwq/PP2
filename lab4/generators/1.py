# Create a generator that generates the squares of numbers up to some number N.

def squares(n):
    for i in range(1, n):
        yield i ** 2
    
for i in squares(10):
    print(i)