import requests
import pytest
import json
import os
import random
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


# One simple role create
@pytest.fixture()
def one_role_create(base_url, book_create):
    role_data = {"name": "zw4bmURxuIp8KsvDPtARWSyO3B20waPD3Cp1opNB5OGnDMBUzjvtHjMVSyQXw5L680NiFNo8JMvO3",
                 "type": "OpTqflMrpj9UmxYHNkUxREjuFT0jEipSh2psVc4UkuQzl9yaYihbPN9y3v6t5nKBRvRUrybxnbKyCxNSfLDW843UmCU6xnvqekel3lbCLhzHE5kIogcU9NOQgFPld9EIVy9NBchYN2i0tdevCTuA35YwfQRlYH1tjx7W3jcGhvWz4zgOunrD0SsqXLn",
                 "level": -31166241,
                 "book": base_url + f"/books/{book_create['id']}"}
    yield role_data
    if 'id' in role_data:
        requests.delete(base_url + f"/roles/{role_data['id']}")


# Read roles data params from JSON file
with open(os.getcwd() + '/json_data/roles_data_list.json', 'r') as file:
    json_data = file.read()
    roles_list = json.loads(json_data)


# Roles create using parametrize, add book value
@pytest.fixture(params=roles_list, ids=[str(i) for i in roles_list])
def roles_create(request, base_url, book_create):
    request.param["book"] = base_url + f"/books/{book_create['id']}"
    yield request.param
    if 'id' in request.param:
        requests.delete(base_url + f"/roles/{request.param['id']}")


# Create list with roles, using same book for all roles
@pytest.fixture()
def roles_list_create(base_url, book_create):
    roles_list_create = [{"name": random_string(200),
                          "type": random_string(255),
                          "level": random.randint(-2147483648, 2147483647),
                          "book": base_url + f"/books/{book_create['id']}"
                          } for _ in range(10)]
    yield roles_list_create
    for i in roles_list_create:
        if 'id' in i:
            requests.delete(base_url + f"/roles/{i['id']}")


# Clear all existing roles
@pytest.fixture()
def clear_all_roles(base_url):
    for role in requests.get(base_url + "/roles").json():
        requests.delete(base_url + f"/roles/{role['id']}")