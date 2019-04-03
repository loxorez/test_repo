import requests
import random
from Home7.test_roles import random_string
import pytest


# Posting roles with the same book, filter verifying
def test_roles_filter_by_book_id(book_create, base_url, roles_list_create):
    for role in roles_list_create:
        role["book"] = base_url + f"/books/{book_create['id']}"
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    book_filter = requests.get(base_url + f"/roles/?book_id={book_create['id']}")
    assert book_filter.status_code == 200
    assert book_filter.json() == roles_list_create


# Posting roles with the same type, filter verifying
def test_roles_filter_by_type(base_url, roles_list_create):
    type_value = random_string(255)
    for role in roles_list_create:
        role["type"] = type_value
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    type_filter = requests.get(base_url + f"/roles/?type={type_value}")
    assert type_filter.status_code == 200
    assert type_filter.json() == roles_list_create


# Posting roles with the same level, filter verifying
def test_roles_filter_by_level(base_url, roles_list_create):
    level_value = random.randint(-2147483648, 2147483647)
    for role in roles_list_create:
        role["level"] = level_value
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    level_filter = requests.get(base_url + f"/roles/?level={level_value}")
    assert level_filter.status_code == 200
    assert level_filter.json() == roles_list_create


# Posting roles with level lower than special level value, filter verifying
def test_roles_filter_by_level_lower_than(clear_all_roles, base_url, roles_list_create, one_role_create):
    filter_min_number = random.randint(-2147483648, 0)
    filter_max_number = random.randint(0, 2147483647)
    for role in roles_list_create:
        role["level"] = random.randint(filter_min_number, filter_max_number-1)
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    one_role_create["level"] = filter_max_number
    role_with_filter_number = requests.post(base_url + f"/roles", data=one_role_create)
    assert role_with_filter_number.status_code == 201
    role_with_filter_number_as_obj = role_with_filter_number.json()
    one_role_create["id"] = role_with_filter_number_as_obj["id"]
    level_filter = requests.get(base_url + f"/roles/?level__lt={filter_max_number}")
    assert level_filter.status_code == 200
    assert role_with_filter_number_as_obj not in level_filter.json()
    assert level_filter.json() == roles_list_create


# Posting roles with level lower or equal than special level value, filter verifying
def test_roles_filter_by_level_lower_or_equal_than(clear_all_roles, base_url, roles_list_create, one_role_create):
    filter_min_number = random.randint(-2147483648, 0)
    filter_max_number = random.randint(0, 2147483647)
    for role in roles_list_create:
        role["level"] = random.randint(filter_min_number, filter_max_number)
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    one_role_create["level"] = filter_max_number
    role_with_filter_number = requests.post(base_url + f"/roles", data=one_role_create)
    assert role_with_filter_number.status_code == 201
    role_with_filter_number_as_obj = role_with_filter_number.json()
    one_role_create["id"] = role_with_filter_number_as_obj["id"]
    level_filter = requests.get(base_url + f"/roles/?level__lte={filter_max_number}")
    assert level_filter.status_code == 200
    roles_list_create.append(role_with_filter_number_as_obj)
    assert level_filter.json() == roles_list_create


# Posting roles with level greater than special level value, filter verifying
def test_roles_filter_by_level_greater_than(clear_all_roles, base_url, roles_list_create, one_role_create):
    filter_min_number = random.randint(-2147483648, 0)
    filter_max_number = random.randint(0, 2147483647)
    for role in roles_list_create:
        role["level"] = random.randint(filter_min_number+1, filter_max_number)
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    one_role_create["level"] = filter_min_number
    role_with_filter_number = requests.post(base_url + f"/roles", data=one_role_create)
    assert role_with_filter_number.status_code == 201
    role_with_filter_number_as_obj = role_with_filter_number.json()
    one_role_create["id"] = role_with_filter_number_as_obj["id"]
    level_filter = requests.get(base_url + f"/roles/?level__gt={filter_min_number}")
    assert level_filter.status_code == 200
    assert role_with_filter_number_as_obj not in level_filter.json()
    assert level_filter.json() == roles_list_create


# Posting roles with level greater or equal than special level value, filter verifying
def test_roles_filter_by_level_greater_or_equal_than(clear_all_roles, base_url, roles_list_create, one_role_create):
    filter_min_number = random.randint(-2147483648, 0)
    filter_max_number = random.randint(0, 2147483647)
    for role in roles_list_create:
        role["level"] = random.randint(filter_min_number, filter_max_number)
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    one_role_create["level"] = filter_min_number
    role_with_filter_number = requests.post(base_url + f"/roles", data=one_role_create)
    assert role_with_filter_number.status_code == 201
    role_with_filter_number_as_obj = role_with_filter_number.json()
    one_role_create["id"] = role_with_filter_number_as_obj["id"]
    level_filter = requests.get(base_url + f"/roles/?level__gte={filter_min_number}")
    assert level_filter.status_code == 200
    roles_list_create.append(role_with_filter_number_as_obj)
    assert level_filter.json() == roles_list_create


# Posting roles in special level value range, filter combining verifying
def test_roles_combine_level_and_book_filters(clear_all_roles, base_url, book_create, roles_list_create):
    filter_min_number = random.randint(-2147483648, 0)
    filter_max_number = random.randint(0, 2147483647)
    for role in roles_list_create:
        role["level"] = random.randint(filter_min_number, filter_max_number)
        role["book"] = base_url + f"/books/{book_create['id']}"
        role_post = requests.post(base_url + "/roles", data=role)
        assert role_post.status_code == 201
        role_as_obj = role_post.json()
        role['id'] = role_as_obj['id']
    book_filter = requests.get(base_url + f"/roles/?level__gt={filter_min_number}&level__lt={filter_max_number}&book_id={book_create['id']}")
    print(book_filter.json())
    assert book_filter.status_code == 200
    assert book_filter.json() == roles_list_create


