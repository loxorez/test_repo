import requests


def test_role_does_not_create_if_no_such_book(base_url, book_create, roles_create):
    book = requests.delete(base_url + f"/books/{book_create['id']}")
    assert book.status_code == 204
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 400
    assert roles_create not in requests.get(base_url + "/roles").json()


def test_role_name_is_required(base_url, roles_create):
    role_name = roles_create["name"]
    roles_create.__delitem__("name")
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 400
    assert roles_create not in requests.get(base_url + "/roles").json()
    roles_create["name"] = role_name


def test_role_type_is_required(base_url, roles_create):
    role_type = roles_create["type"]
    roles_create.__delitem__("type")
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 400
    assert roles_create not in requests.get(base_url + "/roles").json()
    roles_create["type"] = role_type


def test_role_level_is_not_required(base_url, roles_create):
    role_level = roles_create["level"]
    roles_create.__delitem__("level")
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    roles_create["id"], roles_create["level"] = role_as_obj["id"], role_as_obj["level"]
    assert role_as_obj == roles_create
    assert roles_create in requests.get(base_url + "/roles").json()
    delete_role = requests.delete(base_url + f"/roles/{roles_create['id']}")
    assert delete_role.status_code == 204
    roles_create["level"] = role_level


def test_role_book_is_not_required(base_url, roles_create):
    role_book = roles_create["book"]
    roles_create.__delitem__("book")
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    roles_create["id"], roles_create["book"] = role_as_obj["id"], role_as_obj["book"]
    assert role_as_obj == roles_create
    assert roles_create in requests.get(base_url + "/roles").json()
    delete_role = requests.delete(base_url + f"/roles/{roles_create['id']}")
    assert delete_role.status_code == 204
    roles_create["book"] = role_book


def test_role_deleted_if_book_deleted(base_url, book_create, roles_create):
    role = requests.post(base_url + "/roles", data=roles_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    roles_create["id"] = role_as_obj["id"]
    assert role_as_obj == roles_create
    book_delete = requests.delete(base_url + f"/books/{book_create['id']}")
    assert book_delete.status_code == 204
    assert roles_create not in requests.get(base_url + "/roles").json()


