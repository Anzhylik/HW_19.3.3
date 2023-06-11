import requests
import json
import kwargs as kwargs

# GET запрос
base_url = 'https://petstore.swagger.io/v2'
status = 'available'
res_get = requests.get(f"{base_url}/pet/findByStatus?status={status}",
                   headers={'accept': 'application/json'})

print(res_get.status_code)
print(res_get.json())
print(type(res_get.json()))

# POST Запрос

params = {
    'status': 'available'
}

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    'id': 0,
    'username': 'any',
    'firstName': 'bony',
    'lastName': 'tree',
    'email': 'r@bk.ru',
    'password': '123456789',
    'phone': '987654321',
    'userStatus': 0
}

res_post = requests.post(f"{base_url}/user", headers=headers, data=json.dumps(data))

print(res_post.status_code)
print(res_post.json())
print(type(res_post.json()))

# DELETE запрос
username = 'any'
res_delete = requests.delete(f"{base_url}/user/{username}", headers=headers)

print(res_delete.status_code)
print(res_delete.json)
print(type(res_delete.json()))


# PUT запрос

data1 = {
    'id': 0,
    'username': 'a',
    'firstName': 'bony',
    'lastName': 'tree',
    'email': 'r@bk.ru',
    'password': '123456789',
    'phone': '987654321',
    'userStatus': 0
}

res_put = requests.put(f"{base_url}/user/username", headers=headers, data=json.dumps(data))

print(res_put.status_code)
print(res_put.json())
print(type(res_put.json()))
