import json
import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
           params={'AuthorName':'Rahul Shetty2'},)
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(type(dict_response))
# final_res = dict_response[0]['isbn']
# print(final_res)
final_res = response.json()
print(final_res[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
for actualbook in final_res:
    if actualbook['isbn'] == 'CCCC':
        print(actualbook)
        break


expected_book = {
                   'book_name': 'Learn REQUEST WITH POST METHOD',
                    'isbn': '0108',
                    'aisle': '2024'

                 }

print("Actual Book:", actualbook)
print("Expected Book:", expected_book)
assert actualbook == expected_book
