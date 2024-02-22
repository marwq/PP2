# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i
            
for i in divisible_by_3_and_4(100):
    print(i)