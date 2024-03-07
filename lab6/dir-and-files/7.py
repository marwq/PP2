# Write a Python program to copy the contents of a file to another file

from shutil import copyfile

def copy_file(src: str, dst: str):
    copyfile(src, dst)
            
copy_file(r'lab6\dir-and-files\7.py', 'copy.txt')