import unittest
import pytest
from staff import ITEmployee


class TestITEmployee(unittest.TestCase):
    # setUp will be runned before every single test
    def setUp(self):
        self.itemp1 = ITEmployee('Vitalii Kondratiuk', 1989, 'QA', 2, 1000)
        self.itemp2 = ITEmployee('euGENe sYdoRENKO', 1991, 'Developer', 3, 1500)
        self.itemp3 = ITEmployee()

    # tarDown will be runned after every single test
    def tearDown(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.itemp1.full_name, 'Vitalii Kondratiuk')
        self.assertEqual(self.itemp2.full_name, 'Eugene Sydorenko')
        self.assertEqual(self.itemp3.full_name, 'Default Default')
        self.itemp3.full_name = 'Name Surname'
        self.assertEqual(self.itemp3.full_name, 'Name Surname')
        with self.assertRaises(ValueError):
            ITEmployee(full_name='Vitalii Aleksandrovich Kondratiuk')
        with self.assertRaises(ValueError):
            ITEmployee(full_name='Vita333lii Kondratiuk')
        with self.assertRaises(ValueError):
            ITEmployee(full_name='Vitalii Kon33333dratiuk')

    def test_birth_year(self):
        self.assertEqual(self.itemp1.birth_year, 1989)
        self.assertEqual(self.itemp2.birth_year, 1991)
        self.assertEqual(self.itemp3.birth_year, 1900)
        self.itemp3.birth_year = 2000
        self.assertEqual(self.itemp3.birth_year, 2000)
        with self.assertRaises(ValueError):
            ITEmployee(birth_year=2050)
        with self.assertRaises(ValueError):
            ITEmployee(birth_year=1890)

    def test_name(self):
        self.assertIsNotNone(self.itemp1.name())
        self.assertIn(self.itemp1.name(), self.itemp1.full_name)
        self.assertEqual(self.itemp1.name(), 'Vitalii')
        self.assertEqual(self.itemp2.name(), 'Eugene')
        self.assertEqual(self.itemp3.name(), 'Default')
        self.itemp3.full_name = 'Name Surname'
        self.assertEqual(self.itemp3.name(), 'Name')

    def test_surname(self):
        self.assertIsNotNone(self.itemp1.surname())
        self.assertIn(self.itemp1.surname(), self.itemp1.full_name)
        self.assertEqual(self.itemp1.surname(), 'Kondratiuk')
        self.assertEqual(self.itemp2.surname(), 'Sydorenko')
        self.assertEqual(self.itemp3.surname(), 'Default')
        self.itemp3.full_name = 'Name Surname'
        self.assertEqual(self.itemp3.surname(), 'Surname')

    def test_age_in(self):
        self.assertIsNotNone(self.itemp1.age_in())
        self.assertEqual(self.itemp1.age_in(2050), 61)
        self.assertEqual(self.itemp2.age_in(2021), 30)
        self.assertEqual(self.itemp3.age_in(2000), 100)
        self.itemp3.birth_year = 1950
        self.assertEqual(self.itemp3.age_in(), 69)
        with self.assertRaises(ValueError):
            self.itemp1.age_in(1000)

    def test_position(self):
        self.assertEqual(self.itemp1.position, 'QA')
        self.assertEqual(self.itemp2.position, 'Developer')
        self.assertEqual(self.itemp3.position, '')
        self.itemp3.position = 'Project Manager'
        self.assertEqual(self.itemp3.position, 'Project Manager')

    def test_experience(self):
        self.assertEqual(self.itemp1.experience, 2)
        self.assertEqual(self.itemp2.experience, 3)
        self.assertEqual(self.itemp3.experience, 0)
        self.itemp3.experience = 5
        self.assertEqual(self.itemp3.experience, 5)
        with self.assertRaises(ValueError):
            ITEmployee(experience=-3)

    def test_salary(self):
        self.assertEqual(self.itemp1.salary, 1000)
        self.assertEqual(self.itemp2.salary, 1500)
        self.assertEqual(self.itemp3.salary, 0)
        self.itemp3.salary = 2000
        self.assertEqual(self.itemp3.salary, 2000)
        with self.assertRaises(ValueError):
            ITEmployee(salary=-500)

    def test_programmer_level(self):
        self.assertIsNotNone(self.itemp1.programmer_level())
        self.assertEqual(self.itemp1.programmer_level(), 'Junior programmer')
        self.assertEqual(self.itemp2.programmer_level(), 'Middle programmer')
        self.itemp2.experience = 6
        self.assertEqual(self.itemp2.programmer_level(), 'Middle programmer')
        self.assertEqual(self.itemp3.programmer_level(), 'Junior programmer')
        self.itemp3.experience = 7
        self.assertEqual(self.itemp3.programmer_level(), 'Senior programmer')

    def test_salary_raise(self):
        self.assertIsNone(self.itemp1.salary_raise())
        self.assertEqual(self.itemp1.salary, 1050)
        self.itemp1.salary = 1000
        self.itemp1.salary_raise(1.12345)
        self.assertEqual(self.itemp1.salary, 1123)
        with self.assertRaises(ValueError):
            self.itemp1.salary_raise(0)

    def test_skills(self):
        self.assertIsInstance(self.itemp1.skills, list)
        self.assertFalse(self.itemp1.skills)
        self.itemp1.add_skills('Python')
        self.assertEqual(len(self.itemp1.skills), 1)
        self.assertIn('Python', self.itemp1.skills)
        self.itemp1.add_skills('Java', 'git')
        self.assertEqual(len(self.itemp1.skills), 3)
        self.itemp1.add_skills('Python')
        self.assertEqual(self.itemp1.skills, ['Python', 'Java', 'git'])
        self.assertIsNone(self.itemp1.add_skills())

    def test_is_itemployee(self):
        self.assertIsInstance(self.itemp1, ITEmployee)
        self.assertIsInstance(self.itemp2, ITEmployee)


if __name__ == "__main":
    unittest.main()