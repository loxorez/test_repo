#Task 1.1
a = '1989'
b = '1989 year'
print(a.isdigit())
print(b.isdigit())

#Task 1.2-1.3
test_string1 = """
Learning python is so easy if your'e making best effort you can.
Newer give up, no nothing impossible.
"""

print(test_string1.count(" "))
print(test_string1.count("."))

#Task 1.4
test_string2 = 'Hello'
print(test_string2.center(100))

#Task 1.5
print(test_string1.title())

#############################################

#Task 2.1
import math
hypotenuza = math.hypot(179, 971)
print(hypotenuza)

#Task 2.2
test_number = 89
print(test_number//10)

#Task 2.3
test_number2 = 357
test_number2 = str(test_number2)
result = int(test_number2[0])+int(test_number2[1])+int(test_number2[2])
print(result)

#Task 2.4
n = 235
print(n+2) if n % 2 == 0 else print(n+1)

#Task 2.5
x = 537.4584235
print(x % 1)

#Task 2.6
result = str(x).split(".")[1]
result = str(result)[0]
print(result)

#############################################

#Task 3
year = 2016

if year % 4 == 0 and year % 100 != 0:
    print('YES')
elif year % 400 == 0:
    print('YES')
else:
    print('NO')

#Task 4
a = 3
b = 7
c = 9

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

#############################################

#Task 5
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

items = [a, b, c]
items.sort()
a, b, c = items[0], items[1], items[2]
print("{}, {}, {}".format(a, b, c))

#############################################

#Task 6
a = 3
b = 2
c = 2

items = [a, b, c]
if items.count(a) == 3:
    print(3)
elif items.count(a) == 2 or items.count(b) == 2:
    print(2)
else:
    print(0)

#############################################

#Task 7
human = {"Name": "Alex", "Surname": "Miller", "Age": 45, "Phone": {"Mobile": "093-689-23-74", "Work": "044-233-11-45"},
         "Address": "Gagarina 1", "Property": ['Apartment', 'Car', 'Plane']}

human['Age'] += 1
human['Phone']['Mobile'] = "067-123-45-67"
human['Property'].append('Yacht')

print(human)

