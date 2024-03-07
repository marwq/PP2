# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

from pathlib import Path
import stat
import os

def check(path: str):
    p = Path(path)
    st_mode = p.stat().st_mode
    return p.exists() and bool(st_mode & stat.S_IWUSR)

def delete_file(path: str):
    if not check(path):
        return 'Not exists or not writable'
    
    Path(path).unlink()
    return 'Deleted'

path = input('Enter a path: ')
print(delete_file(path))