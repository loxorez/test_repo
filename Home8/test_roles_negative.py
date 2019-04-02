import requests


# Try to create if no such book
def test_role_does_not_create_if_no_such_book(base_url, book_create, one_role_create):
    book = requests.delete(base_url + f"/books/{book_create['id']}")
    assert book.status_code == 204
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 400
    assert one_role_create not in requests.get(base_url + "/roles").json()


# Try to create role without name
def test_role_name_is_required(base_url, one_role_create):
    role_name = one_role_create["name"]
    one_role_create.__delitem__("name")
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 400
    assert one_role_create not in requests.get(base_url + "/roles").json()
    one_role_create["name"] = role_name


# Try to create role without type
def test_role_type_is_required(base_url, one_role_create):
    role_type = one_role_create["type"]
    one_role_create.__delitem__("type")
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 400
    assert one_role_create not in requests.get(base_url + "/roles").json()
    one_role_create["type"] = role_type


# Try to create role without level
def test_role_level_is_not_required(base_url, one_role_create):
    role_level = one_role_create["level"]
    one_role_create.__delitem__("level")
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    one_role_create["id"], one_role_create["level"] = role_as_obj["id"], role_as_obj["level"]
    assert role_as_obj == one_role_create
    assert one_role_create in requests.get(base_url + "/roles").json()
    delete_role = requests.delete(base_url + f"/roles/{one_role_create['id']}")
    assert delete_role.status_code == 204
    one_role_create["level"] = role_level


# Try to create role without book
def test_role_book_is_not_required(base_url, one_role_create):
    role_book = one_role_create["book"]
    one_role_create.__delitem__("book")
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    one_role_create["id"], one_role_create["book"] = role_as_obj["id"], role_as_obj["book"]
    assert role_as_obj == one_role_create
    assert one_role_create in requests.get(base_url + "/roles").json()
    delete_role = requests.delete(base_url + f"/roles/{one_role_create['id']}")
    assert delete_role.status_code == 204
    one_role_create["book"] = role_book


# Role is not deleted if book was delete
def test_role_is_not_deleted_if_book_deleted(base_url, book_create, one_role_create):
    role = requests.post(base_url + "/roles", data=one_role_create)
    assert role.status_code == 201
    role_as_obj = role.json()
    one_role_create["id"] = role_as_obj["id"]
    assert role_as_obj == one_role_create
    book_delete = requests.delete(base_url + f"/books/{book_create['id']}")
    assert book_delete.status_code == 204
    one_role_create['book'] = None
    assert one_role_create in requests.get(base_url + "/roles").json()
    role_delete = requests.delete(base_url + f"/roles/{one_role_create['id']}")
    assert role_delete.status_code == 204
