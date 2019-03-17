import requests

base_roles_url = 'http://pulse-rest-testing.herokuapp.com/roles'

# Создаёт персонажа POST /roles/, вы запоминаете его id.
ch_post = requests.post(base_roles_url, data={"name": "Robi",
                                              "type": "Human",
                                              "level": 1,
                                              "book": 104})
object = ch_post.json()
id = object['id']
print(ch_post.ok)

# Проверяете, что он создался и доступен по ссылке GET /roles/[id]
ch_get = requests.get(base_roles_url + f"/{id}")
print(ch_get.json())

# Проверяете, что он есть в списке пользователей по GET /roles/
ch_get = requests.get(base_roles_url)
print(object in ch_get.json())

# Изменяете этого пользователя методом PUT roles/[id]/
ch_put = requests.put(base_roles_url + f"/{id}", data={"name": "Monkey",
                                                       "type": "Animal",
                                                       "level": 2,
                                                       "book": None})
updated_object = ch_put.json()
print(ch_put.ok)

# Проверяете, что он изменился и доступен по ссылке /roles/[id]
ch_get = requests.get(base_roles_url + f"/{id}")
print(ch_get.json())

# Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
ch_get = requests.get(base_roles_url)
print(updated_object in ch_get.json())

# Удаляете этого пользователя методом DELETE roles/[id]
ch_del = requests.delete(base_roles_url + f"/{id}")
print(ch_del.ok)