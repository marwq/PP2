# Write a Python program to count the number of lines in a text file.

def count_lines(path: str):
    count = 0
    with open(path, encoding='utf8') as f:
        for _ in f.readlines():
            count += 1
    return count

file = input('Enter a path of text file: ')
print(f'Lines: {count_lines(file)}')