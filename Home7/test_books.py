import unittest
import requests


class TestBooks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book_id = None

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com'
        self.book_data = {"author": "Charles Dickens",
                          "title": "Oliver Twist",}

    def tearDown(self):
        pass

    def test_1_book_created(self):
        book_data = {"author": "Charles Dickens",
                     "title": "Oliver Twist"}
        book = requests.post(self.base_url + "/books", data=self.book_data)
        book_as_obj = book.json()
        book_id = book_as_obj['id']
        self.assertEqual(book.status_code, 201)
        self.assertIn(book_as_obj, requests.get(self.base_url + "/books").json())
        TestBooks.book_id = book_id

    def test_2_book_read(self):
        book = requests.get(self.base_url + "/books" + f"/{TestBooks.book_id}")
        self.assertEqual(book.status_code, 200)
        self.book_data['id'] = TestBooks.book_id
        self.assertDictEqual(self.book_data, book.json())

    def test_3_book_update(self):
        book_data = {"author": "Jane Austen",
                     "title": "Pride and Prejudice"}
        book = requests.put(self.base_url + "/books" + f"/{TestBooks.book_id}", data=book_data)
        book_as_obj = book.json()
        self.assertEqual(book.status_code, 200)
        self.assertIn(book_as_obj, requests.get(self.base_url + "/books").json())

    def test_4_book_delete(self):
        book = requests.delete(self.base_url + "/books" + f"/{TestBooks.book_id}")
        self.assertEqual(book.status_code, 204)
        self.assertEqual(requests.get(self.base_url + "/book" + f"/{TestBooks.book_id}").status_code, 404)

    # def test_delete(self):
    #     books = requests.get(self.base_url + "/books")
    #     for i in books.json():
    #         requests.delete(self.base_url + f"/books/{i['id']}")

if __name__ == "__main__":
    unittest.main(verbosity=2)

