import requests
import random
from Home7.test_roles import random_string


# Posting roles with the same book, filter verifying, roles clearing
def test_roles_filter_by_book_id(book_create, base_url, roles_list_create):
    roles_list = roles_list_create
    for role in roles_list:
        role["book"] = base_url + f"/books/{book_create['id']}"
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    book_filter = requests.get(base_url + f"/roles/?book_id={book_create['id']}")
    assert book_filter.status_code == 200
    assert book_filter.json() == roles_list
    for role in roles_list:
        role_delete = requests.delete(base_url + f"/roles/{role['id']}")
        assert role_delete.status_code == 204


# Posting roles with the same type, filter verifying, roles clearing
def test_roles_filter_by_type(base_url, roles_list_create):
    roles_list = roles_list_create
    type_value = random_string(255)
    for role in roles_list:
        role["type"] = type_value
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    type_filter = requests.get(base_url + f"/roles/?type={type_value}")
    assert type_filter.status_code == 200
    assert type_filter.json() == roles_list
    for role in roles_list:
        role_delete = requests.delete(base_url + f"/roles/{role['id']}")
        assert role_delete.status_code == 204


# Posting roles with the same level, filter verifying, roles clearing
def test_roles_filter_by_level(base_url, roles_list_create):
    roles_list = roles_list_create
    level_value = random.randint(-2147483648, 2147483647)
    for role in roles_list:
        role["level"] = level_value
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    level_filter = requests.get(base_url + f"/roles/?level={level_value}")
    assert level_filter.status_code == 200
    assert level_filter.json() == roles_list
    for role in roles_list:
        role_delete = requests.delete(base_url + f"/roles/{role['id']}")
        assert role_delete.status_code == 204
