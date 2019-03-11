import datetime


class Person():
    def __init__(self, full_name, birth_year):
        if len(full_name.split()) != 2:
            raise ValueError('full_name should consist of name and surname separated by space')
        if not ''.join(full_name.split()).isalpha():
            raise ValueError('full_name can not contain digits')
        if birth_year < 1900 or birth_year > datetime.datetime.now().year:
            raise ValueError(f'birt_year acceptable range is 1900-{datetime.datetime.now().year}')
        self.full_name = full_name.title()
        self.birth_year = birth_year

    def name(self):
        return self.full_name.split()[0]

    def surname(self):
        return self.full_name.split()[1]

    def age_in(self, year=datetime.datetime.now().year):
        if year < self.birth_year:
            raise ValueError('Year should be greater or equal to birth_year')
        return year - self.birth_year


class Employee(Person):
    def __init__(self, full_name='Default Default', birth_year=1900, position='', experience=0, salary=0):
        if experience < 0 or salary < 0:
            raise ValueError('experiance or salary is negative')

        super().__init__(full_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary

    def programmer_level(self):
        if self.experience < 3:
            return 'Junior programmer'
        if self.experience >= 3 and self.experience <= 6:
            return 'Middle programmer'
        if self.experience > 6:
            return 'Senior programmer'

    def salary_raise(self, amount=1.05):
        if amount < 1:
            raise ValueError("you can't decrease salary")
        self.salary *= amount
        self.salary = int(self.salary)


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skills(self, *new_skills):
        for skill in new_skills:
            if skill in self.skills:
                continue
            self.skills.append(skill)


    def __str__(self):
        return f"{self.full_name} was born in {self.birth_year}({self.age_in()} years old)," \
            f" take a '{self.position}' position with {self.experience} years work experience" \
            f" and {', '.join(self.skills)} skills. \nProfessional level is {self.programmer_level()}"

#
# p1 = Person('Vitalii Kondratiuk', 1989)
# print(p1.name())
# print(p1.surname())
# print(p1.age_in())
#
# e1 = Employee('Andrii Kushnir', 1980, 'Team Lead', 5, 3000)
# print(e1.full_name, e1.birth_year, e1.position, e1.experience, e1.salary)
# print(e1.programmer_level())
# e1.salary_raise()
# print(e1.salary)
#
# ite1 = ITEmployee('Evgen Sydorenko', 1990, 'Developer', 3, 1500)
# print(ite1.full_name, ite1.programmer_level(), ite1.skills)
# ite1.add_skills('Java', 'Python')
# print(ite1.skills)
# print(ite1)