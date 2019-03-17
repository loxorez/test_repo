import requests

base_books_url = 'http://pulse-rest-testing.herokuapp.com/books'

# Создаёт книгу POST /books/, вы запоминаете её id.
bk_post = requests.post(base_books_url, data={"author": "Charles Dickens",
                                              "title": "Oliver Twist",})
object = bk_post.json()
id = object['id']
print(bk_post.ok)

# Проверяете, что она создалась и доступна по ссылке GET /books/[id]
bk_get = requests.get(base_books_url + f"/{id}")
print(bk_get.json())

# Проверяете, что она есть в списке книг по GET /books/
bk_get = requests.get(base_books_url)
print(object in bk_get.json())

# Изменяете эту книгу методом PUT books/[id]/
bk_put = requests.put(base_books_url + f"/{id}", data={"author": "Jane Austen",
                                                       "title": "Pride and Prejudice"})
update_object = bk_put.json()
print(bk_put.ok)

# Проверяете, что она изменилась и доступна по ссылке /books/[id]
bk_get = requests.get(base_books_url + f"/{id}")
print(bk_get.json())

# Проверяете, что книга есть в списке книг по GET /books/ с новой инфой
bk_get = requests.get(base_books_url)
print(update_object in bk_get.json())

# Удаляете эту кингу методом DELETE books/[id]
bk_del = requests.delete(base_books_url + f"/{id}")
print(bk_del.ok)