# Write a Python program to list only directories, files and all directories, files in a specified path.

from pathlib import Path

def list_directories_files(path: str):
    p = Path(path)
    return (
        [x.name for x in p.iterdir() if x.is_dir()],
        [x.name for x in p.iterdir() if x.is_file()]
    )
    
path = input('Enter a path: ')
dirs, files = list_directories_files(path)

print(f'Directories:', *dirs, sep='\n')
print(f'\nFiles:', *files, sep='\n')