# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

from pathlib import Path

def test_path(path: str):
    p = Path(path)
    yield p.exists()
    if p.exists():
        yield p.name
        yield p.parent

path = input('Enter a path: ')
res = test_path(path)

is_exists = next(res)
print(f'Exists: {is_exists}')

if is_exists:
    print(f'Name: {next(res)}')
    print(f'Parent: {next(res)}')