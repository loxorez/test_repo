"""
Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки
колонок)
 Посчитайте сколько отделов на фирме
 Определите максимальную зарплату
 Определите максимальную зарплату в каждом отделе
 Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
новый файл
"""

import xlrd


class Person(object):
    class_objects = []

    def __init__(self, surname, name, department, salary):
        self.surname = surname
        self.name = name
        self.department = department
        self.salary = salary
        Person.class_objects.append(self)

    @classmethod
    def departments_count(cls):
        """
        Count all departments
        :return: departments value
        """
        departments_list  = []
        for person in cls.class_objects:
            if person.department not in departments_list:
                departments_list.append(person.department)
        return len(departments_list)

    @classmethod
    def max_salary(cls):
        """
        Count max salary
        :return: max salary
        """
        salary_list = []
        for person in cls.class_objects:
            salary_list.append(person.salary)
        return max(salary_list)

    @classmethod
    def max_salary_in_department(cls):
        """
        Count max salary in department
        :return: Dict in format "department": salary
        """
        department_max_sallary = {}
        for person in cls.class_objects:
            if person.department not in department_max_sallary:
                department_max_sallary[person.department] = person.salary
            elif department_max_sallary[person.department] < person.salary:
                department_max_sallary[person.department] = person.salary
        return department_max_sallary

    @classmethod
    def person_with_max_salary_in_department(cls):
        """
        Return objects with max salary in each department
        :return: list of objects with max salary in department
        """
        max_salary_in_department = cls.max_salary_in_department()
        persons_with_max_salary = []
        for person in cls.class_objects:
            if person.salary == max_salary_in_department[person.department]:
                persons_with_max_salary.append(person)
        return persons_with_max_salary


def table_as_list(filename):
    """
    Open database file, unpack all rows and columns data in list format
    :param filename: path to file
    :return: list with every rows data as list
    """
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)

    table = []
    line_records = []

    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            line_records.append(sheet.cell(row, col).value)
        table.append(line_records)
        line_records = []
    return table


if __name__ == "__main__":
    table = table_as_list('/home/qa/My_project/test_repo/Home6/Files to work with/Workers_database.xlsx')
    for i in table[1::]:
        Person(i[0], i[1], i[2], i[3])

dest_file = open('/home/qa/My_project/test_repo/Home6/Files to work with/Max_salary_in_department_result.txt', 'w')
for person in Person.person_with_max_salary_in_department():
    print("{:<15} {:<10.0f} {:<15}".format(person.department, person.salary, person.surname), file=dest_file)
dest_file.close()


