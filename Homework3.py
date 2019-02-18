#!/usr/bin/python3

#Task 1

user_input = input('Enter your line: ')
#user_input = "The United States is asking Britain, France, Germany and other European allies to take back over 800 ISIS fighters that we captured in Syria and put them on trial. "

try:
      splited_user_input = user_input.split()
      third_symbol = user_input[2]
      symbol_before_last_one = splited_user_input[1][-2]
      first_five_symbols = splited_user_input[2][:5]
      entirely_fourth_word = splited_user_input[3][:-2:]
      all_even_in_five_line = splited_user_input[4][::2]
      all_uneven_in_six = splited_user_input[5][1::2]
      reversed_seven = splited_user_input[6][::-1]
      reversed_eight_step = splited_user_input[7][-1::-2]
      nine_reversed = splited_user_input[8][-2:0:-1]
      whole_line_len = len(user_input)
except IndexError:
      print('IndexError was found')
else:
      print(third_symbol, symbol_before_last_one, first_five_symbols, entirely_fourth_word, all_even_in_five_line,
      all_uneven_in_six, reversed_seven, reversed_eight_step, nine_reversed, whole_line_len, sep='\n')


#Task 2

user_input = input('Enter your line: ')
#user_input = "The United States is asking Britain, France, Germany and other European allies to take back over 800 ISIS fighters that we captured in Syria and put them on trial. "

second_part_len = len(user_input) // 2
first_part_len = len(user_input) - second_part_len
new_line = user_input[first_part_len + 1:] + user_input[:first_part_len + 1]
print(new_line)

#Task 3

count = 0
while count <= 10:
    print(count)
    count += 1


count = 20
list_with_step = []
while count >= 1:
    list_with_step.append(str(count))
    count -= 1
print(' '.join(list_with_step))


number = 1024
devide_count = 0
if number % 2 == 0:
    while number > 0 and number % 2 == 0:
        number /= 2
        devide_count += 1
print(devide_count)

#Task 4

my_list = ['The', 'United', 'States', 'is', 'asking', 'Britain,', 'France,', 'Germany']
while my_list:
    print(my_list.pop(0))


user_line = "The United States is asking Britain, France, Germany and other European allies to take back over 800 ISIS fighters that we captured in Syria and put them on trial. "
while len(user_line):
    print(user_line[0])
    user_line = user_line[1:]


my_list = ['The', 'United', 'States', 'is', 'asking', 'Britain,', 'France,', 'Germany']
my_list = sorted(my_list)
while my_list:
    print(my_list.pop(0))

#Task 5

first = input('Enter first value: ')
second = input('Enter second value: ')

try:
    result = float(first) + float(second)
except ValueError:
    result = str(first) + str(second)
else:
    if result % 1 == 0:
        result = int(result)
finally:
    print("Result is : ", result)

#Task 6

def is_year_leap(year):
    """
    To verify if year is leap
    :param year: int, year format
    :return: bool, result
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def is_triangle_exist(a, b, c):
    """
    Function checks exists triangle or not
    :param a: int, first side
    :param b: int, second side
    :param c: int, thirst side
    :return: bool, result
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def no_space_inside():
    """
    Function prevent user from entering few words in one line
    :return:str, user word cleaned from spaces
    """
    while True:
        user_input = input("Enter your word: ")
        if ' ' in user_input.strip():
            print("Out of conditions. Try again! ")
        else:
            break
    return user_input.strip()


def is_number():
    """
    Checks if user input is digits
    :return: int, user input
    """
    while True:
        user_input = input("Enter your number: ")
        if not user_input.isdigit():
            print("Not digit. Try again! ")
        else:
            return int(user_input)


def triangle_type(a, b, c):
    """
    Determine triangle type
    :param a: int, first side
    :param b: int, second side
    :param c: int, thirst side
    :return: str, triangle type
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or b == c or c == a:
            return 'Isosceles triangle'
        elif a != b and a != c and b != c:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'


def distance_result():
    """
    Measure distance between points that typed user
    :return: tuple, (x1 - y1 distance, x2 - y2 distance)
    """
    def is_value_digit(value):
        """
        Persuade user to type correct distance value in digit format
        :param value: point variable name
        :return: int, user value
        """
        while True:
            user_input = input(f'Enter {value} value: ')
            if not user_input.isdigit():
                print(f'Wrong value {value}. Only digits allowable. Try again.')
            else:
                return int(user_input)

    def distance(first, second):
        """
        Measure distance between two points, no matter which of them is higher
        :param first: int, first point that user typed
        :param second: int, second point that user typed
        :return: int, distance
        """
        if first >= second:
            result = first - second
        else:
            result = second - first
        return result

    x1 = is_value_digit('x1')
    y1 = is_value_digit('y1')
    x2 = is_value_digit('x2')
    y2 = is_value_digit('y2')

    x1_y1_distance = distance(x1, y1)
    x2_y2_distance = distance(x2, y2)

    return x1_y1_distance, x2_y2_distance

#Task 7

user_line = '''
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
'''

word_list = user_line.split()
word_quantity = len(word_list)

for i in range(len(word_list)):
    word_list[i] = word_list[i].strip('.')
    word_list[i] = word_list[i].strip(',')
    word_list[i] = word_list[i].strip('!')

sorted_words = sorted(word_list)

words_counter = {}
for i in sorted_words:
    if i not in words_counter:
        words_counter[i] = 1
    else:
        words_counter[i] += 1
