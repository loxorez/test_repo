"""
Задание из класса «Записываем “Number: строка из файла” из одного файла в
другой»:
"""

directory = '/home/qa/My_project/test_repo/Home6/Files to work with/'

#1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл (кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
object, subject = None, None
try:
    object = open(directory + 'A_Long_Goodbye-Raymond_Chandler.txt', 'r')
    subject = open(directory + 'With_Line_Numbers.txt', 'w')
    for number, line in enumerate(object):
        subject.write(f"{number}: {line}")
        # Uncomment next line to write to subject via print method
        # print(f"{number}: {line.strip()}", file=subject)
except FileNotFoundError:
    print('File not found')
finally:
    if object is not None:
        object.close()
    if subject is not None:
        subject.close()


# 2. Воспользуйтесь менеджером контекста для файла (with … as), в который вы записываете информацию.
try:
    with open(directory + 'A_Long_Goodbye-Raymond_Chandler.txt', 'r') as object, open(directory + 'With_Line_Numbers.txt', 'w') as subject:
        for number, line in enumerate(object):
            subject.write(f"{number}: {line}")
            # Uncomment next line to write to subject via print method
            # print(f"{number}: {line.strip()}", file=subject)
except FileNotFoundError:
    print('File not found')
