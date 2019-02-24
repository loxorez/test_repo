#!usr/bin/python3

#Task1


def sing_gen(line_value = 3, la_value = 3, end = 0):
    """
    Generates and returns la-la-la song as string

    :param line_value: int, how many lines to generate
    :param la_value: int, la counts in single line
    :param end: int, last line last symbol
    :return: str, full song
    """
    full_song = ''
    assert type(line_value) is type(la_value) is type(end) is int, "Only int type is possible as argument's value"
    for line in range(1, line_value+1):
        if line != line_value:
            full_song += 'la-' * (la_value-1) + 'la\n'
        elif line == line_value and end == 0:
            full_song += 'la-' * (la_value-1) + 'la.'
        elif line == line_value and end == 1:
            full_song += 'la-' * (la_value-1) + 'la!'
    return full_song


#Task 2


def second_max(*args):
    """
    Returns the second one value from the min to max order

    :param args: int or str, arguments
    :return: the second one highest value
    """
    args = set(args)
    try:
        args = sorted(list(args))
    except TypeError:
        print('All entered args should have the same type')
    else:
        return args[1]


#Task 3


from modules.string1 import main as string_module
from modules.list1 import main as list_module

if __name__ == "__main__":
    string_module()
    print()
    list_module()
