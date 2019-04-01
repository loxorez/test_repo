import requests
import pytest
import json
import os
from Home7.test_roles import random_string


@pytest.fixture(scope='module')
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com'

# Book create
@pytest.fixture()
def book_create(base_url):
    book_data = {"author": random_string(50),
                 "title": random_string(50)}
    book = requests.post(base_url + f"/books", data=book_data)
    book_body = book.json()
    yield book_body
    if 'id' in book_body:
        requests.delete(base_url + f"/books/{book_body['id']}")


# Read roles data params from JSON file
with open(os.getcwd() + '/json_data/roles_data_list.json', 'r') as file:
    json_data = file.read()
    roles_list = json.loads(json_data)


# Roles create using parametrize, add book value
@pytest.fixture(params=roles_list, ids=[str(i) for i in roles_list])
def roles_create(request, base_url, book_create):
    request.param["book"] = base_url + f"/books/{book_create['id']}"
    yield request.param

