import sys
from Homework4 import sing_gen



with open('song_inside.txt', 'w') as file:
    file.write(sing_gen())
    print('\nHELLO', file=file)

with open('/home/qa/My_project/test_repo/Home4/test_staff.py') as file:
    print(file.read())


