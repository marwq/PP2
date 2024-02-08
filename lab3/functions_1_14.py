# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.

from .functions_1 import has_33, spy_game, sphere_volume, unique_elements, is_palindrome, histogram

def main():
    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(has_33([3, 1, 3]))

    print(spy_game([1,2,4,0,0,7,5]))
    print(spy_game([1,0,2,4,0,5,7]))
    print(spy_game([1,7,2,0,4,5,0]))

    print(sphere_volume(3))

    print(unique_elements([1, 2, 3, 4, 4, 3, 2, 1]))

    print(is_palindrome('madam'))
    print(is_palindrome('hello'))

    histogram([4, 9, 7])
    
if __name__ == '__main__':
    main()