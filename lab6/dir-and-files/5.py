# Write a Python program to write a list to a file.

def list_to_text(list_: list):
    return '\n'.join(list_)

def write_to_file(file: str, list_: list):
    with open(file, encoding='utf8', mode='w') as f:
        f.write(list_to_text(list_))
        
write_to_file(
    'a.txt', 
    ['Hello', 'World']
)