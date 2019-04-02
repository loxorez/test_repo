import pytest
import requests
import random
from Home7.test_roles import random_string


# Create different roles
def test_role_create(base_url, roles_create):
    role = requests.post(base_url + f"/roles", data=roles_create)
    assert role.status_code == 201
    role_body = role.json()
    roles_create['id'] = role_body['id']
    assert roles_create == role_body


# Read different roles
def test_role_read(base_url, roles_create):
    role = requests.post(base_url + f"/roles", data=roles_create)
    assert role.status_code == 201
    role_body = role.json()
    roles_create['id'] = role_body['id']
    role_read = requests.get(base_url + f"/roles/{role_body['id']}")
    assert role_body == role_read.json()


# Update one created role with different data, book stays the same
def test_role_update(base_url, book_create, roles_create):
    role_data = {"name": random_string(200),
                 "type": random_string(255),
                 "level": random.randint(-2147483648, 2147483647),
                 "book": base_url + f"/books/{book_create['id']}"}
    role = requests.post(base_url + f"/roles", data=role_data)
    assert role.status_code == 201
    role_body = role.json()
    roles_create['id'] = role_body['id']
    assert role_data != roles_create
    role_update = requests.put(base_url + f"/roles/{role_body['id']}", data=roles_create)
    assert role_update.status_code == 200
    role_update_body = role_update.json()
    assert role_update_body == roles_create


# Delete different roles
def test_role_delete(base_url, roles_create):
    role = requests.post(base_url + f"/roles", data=roles_create)
    assert role.status_code == 201
    role_body = role.json()
    role_read = requests.get(base_url + f"/roles/{role_body['id']}")
    assert role_body == role_read.json()
    role_delete = requests.delete(base_url + f"/roles/{role_body['id']}")
    assert role_delete.status_code == 204
    assert role_body not in requests.get(base_url + "/roles").json()