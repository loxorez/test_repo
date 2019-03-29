import unittest
import requests
import random
import string
from HtmlTestRunner import HTMLTestRunner


def random_string(string_len):
    """
    Create a string using random characters
    :param string_len: string is expected to be generated in range
    :return: string with random cases characters
    """
    ascii_let_dig = string.ascii_letters + string.digits
    string_result = "".join(random.choices(ascii_let_dig, k=random.randint(1, string_len)))
    return string_result


class TestRoles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # for i in requests.get('http://pulse-rest-testing.herokuapp.com/roles').json():
        #     requests.delete(f"http://pulse-rest-testing.herokuapp.com/roles/{i['id']}")
        #
        # for i in requests.get('http://pulse-rest-testing.herokuapp.com/books').json():
        #     requests.delete(f"http://pulse-rest-testing.herokuapp.com/books/{i['id']}")
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.base_books_url = 'http://pulse-rest-testing.herokuapp.com/books'
        self.base_roles_url = 'http://pulse-rest-testing.herokuapp.com/roles'
        self.book = requests.post(self.base_books_url,
                                  data={'author': random_string(50),
                                        'title': random_string(50)})
        if self.book.status_code == 201:
            self.book_id = self.book.json()['id']
        else:
            self.book_id = None

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(self.base_books_url + f"/{self.book_id}")

    def test_role_create(self):
        for _ in range(10):
            role_data = {"name": random_string(200),
                         "type": random_string(255),
                         "level": random.randint(-2147483648, 2147483647),
                         "book": self.book_id}
            with self.subTest(role_data):
                role = requests.post(self.base_roles_url, data=role_data)
                self.assertEqual(role.status_code, 201)
                self.assertIn(role.json(), requests.get(self.base_roles_url).json())

    def test_role_read(self):
        for _ in range(10):
            role_data = {"name": random_string(200),
                         "type": random_string(255),
                         "level": random.randint(-2147483648, 2147483647),
                         "book": self.book_id}
            with self.subTest(role_data):
                role = requests.post(self.base_roles_url, data=role_data)
                self.assertEqual(role.status_code, 201)
                role_as_obj = role.json()
                role_data['id'] = role_as_obj['id']
                role = requests.get(self.base_roles_url + f"/{role_as_obj['id']}")
                self.assertEqual(role.ok, True)
                self.assertDictEqual(role.json(), role_data)
                self.assertIn(role.json(), requests.get(self.base_roles_url).json())

    def test_role_update(self):
        role_data = {"name": random_string(200),
                     "type": random_string(255),
                     "level": random.randint(-2147483648, 2147483647),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 201)
        self.assertIn(role.json(), requests.get(self.base_roles_url).json())
        role_as_obj = role.json()

        for _ in range(10):
            new_role_data = {"name": random_string(200),
                             "type": random_string(255),
                             "level": random.randint(-2147483648, 2147483647),
                             "book": self.book_id}
            with self.subTest(new_role_data):
                role = requests.put(self.base_roles_url + f"/{role_as_obj['id']}", data=new_role_data)
                self.assertEqual(role.status_code, 200)
                new_role_data['id'] = role_as_obj['id']
                self.assertDictEqual(role.json(), new_role_data)
                self.assertIn(role.json(), requests.get(self.base_roles_url).json())

    def test_role_delete(self):
        for _ in range(10):
            role_data = {"name": random_string(200),
                         "type": random_string(255),
                         "level": random.randint(-2147483648, 2147483647),
                         "book": self.book_id}
            with self.subTest(role_data):
                role = requests.post(self.base_roles_url, data=role_data)
                self.assertEqual(role.status_code, 201)
                self.assertIn(role.json(), requests.get(self.base_roles_url).json())
                role_as_obj = role.json()

                role = requests.delete(self.base_roles_url + f"/{role_as_obj['id']}")
                self.assertEqual(role.status_code, 204)
                self.assertNotIn(role_as_obj, requests.get(self.base_roles_url).json())


class TestRolesOptionsAndNegative(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.base_books_url = 'http://pulse-rest-testing.herokuapp.com/books'
        self.base_roles_url = 'http://pulse-rest-testing.herokuapp.com/roles'
        self.book = requests.post(self.base_books_url,
                                  data={"author": random_string(50),
                                        "title": random_string(50)})
        if self.book.status_code == 201:
            self.book_id = self.book.json()['id']
        else:
            self.book_id = None

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(self.base_books_url + f"/{self.book_id}")

    def test_role_does_not_create_if_no_such_book(self):
        book = requests.delete(self.base_books_url + f"/{self.book_id}")
        self.assertEqual(book.status_code, 204)
        role_data = {"name": random_string(200),
                     "type": random_string(255),
                     "level": random.randint(-2147483648, 2147483647),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 400)
        self.assertNotIn(role_data, requests.get(self.base_roles_url).json())
        self.book_id = None

    def test_role_name_is_required(self):
        role_data = {"type": random_string(255),
                     "level": random.randint(-2147483648, 2147483647),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 400)
        self.assertNotIn(role_data, requests.get(self.base_roles_url).json())

    def test_role_type_is_required(self):
        role_data = {"name": random_string(200),
                     "level": random.randint(-2147483648, 2147483647),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 400)
        self.assertNotIn(role_data, requests.get(self.base_roles_url).json())

    def test_role_level_is_not_required(self):
        role_data = {"name": random_string(200),
                     "type": random_string(255),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 201)
        role_as_obj = role.json()
        self.assertIn(role_as_obj, requests.get(self.base_roles_url).json())
        role_delete = requests.delete(self.base_roles_url + f"/{role_as_obj['id']}")
        self.assertEqual(role_delete.status_code, 204)

    def test_role_book_is_not_required(self):
        role_data = {"name": random_string(200),
                     "type": random_string(255),
                     "level": random.randint(-2147483648, 2147483647)}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 201)
        role_as_obj = role.json()
        self.assertIn(role_as_obj, requests.get(self.base_roles_url).json())
        role_delete = requests.delete(self.base_roles_url + f"/{role_as_obj['id']}")
        self.assertEqual(role_delete.status_code, 204)

    def test_role_deleted_if_book_deleted(self):
        role_data = {"name": random_string(200),
                     "type": random_string(255),
                     "level": random.randint(-2147483648, 2147483647),
                     "book": self.book_id}
        role = requests.post(self.base_roles_url, data=role_data)
        self.assertEqual(role.status_code, 201)
        self.assertIn(role.json(), requests.get(self.base_roles_url).json())
        book_delete = requests.delete(self.base_books_url + f"/{self.book_id}")
        self.assertEqual(book_delete.status_code, 204)
        self.assertNotIn(role.json(), requests.get(self.base_roles_url).json())
        self.book_id = None


if __name__ == "__main__":
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(output='/home/qa/My_project/test_repo/Home7/HTML_Report'))

    #suite1 = unittest.TestLoader().loadTestsFromTestCase(TestRoles)
    #result = unittest.TestResult()
    #print(suite1.run(result))

    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestRolesOptionsAndNegative)
    # result2 = unittest.TestResult()
    # print(suite2.run(result))
