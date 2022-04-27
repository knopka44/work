import json
import requests
from pprint import pprint

# GET 1
authors_list = requests.get(
    "https://fakerestapi.azurewebsites.net/api/v1/Authors").json()
pprint(authors_list)

# GET 2
author_id55 = requests.get(
    "https://fakerestapi.azurewebsites.net/api/v1/Authors/55").json()
print(author_id55)

# POST 1
new_book = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books",
                         json={
                             'id': '1000', 'title': 'Here I am',
                             'description': 'Moments do not last forever',
                             'pageCount': '236', 'excerpt': '-',
                             'publishDate': "2008-04-15T15:22:46.574Z"
                         }).json()
pprint(new_book)

# POST 2
new_user = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Users",
                         json={
                             "id": 555, "userName": "Alex Koreev",
                             "password": "alexkor1994lala"
                         }).json()
print(new_user)

# PUT
book10_update = requests.put(
    "https://fakerestapi.azurewebsites.net/api/v1/Books/10",
    json={'id': '10', 'title': 'A walk to remember',
          'description': 'The novel, set in 1958–1959 in Beaufort, '
                         'North Carolina, is a story of two teenagers who fall'
                         ' in love with each other despite the disparity of '
                         'their personalities',
          'pageCount': '240',
          'excerpt': 'Anyway, he wrote this play called The Christmas Angel,'
                     ' because he did not want to keep on performing that old'
                     ' Charles Dickens classic A Christmas Carol',
          'publishDate': "1999-10-08T15:22:46.574Z"}).json()
print(book10_update)

# DELETE
delete_user_id4 = requests.delete(
    "https://fakerestapi.azurewebsites.net/api/v1/Users/4")
assert delete_user_id4.status_code == 200, \
    f"Failed to request. Response: {delete_user_id4}"
