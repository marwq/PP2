# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import stat
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Access:
    exists: bool
    is_executable: bool
    is_readable: bool
    is_writable: bool

def check_access(path: str) -> Access:
    p = Path(path)
    st_mode = p.stat().st_mode
    return Access(
        exists=p.exists(),
        is_executable=bool(st_mode & stat.S_IXUSR),
        is_readable=bool(st_mode & stat.S_IRUSR),
        is_writable=bool(st_mode & stat.S_IWUSR)
    )
    
path = input('Enter a path: ')
access = check_access(path)
print(f'Exists: {access}')