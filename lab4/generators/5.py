# Implement a generator that returns all numbers from (n) down to 0.

def numbers_down_to_zero(n):
    for i in range(n, -1, -1):
        yield i
        
print(list(numbers_down_to_zero(10)))