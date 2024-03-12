import requests
import json

response=requests.get('http://216.10.245.166/Library/GetBook.php',
            params={'AuthorName':'Rahul shetty'})

json_response = response.json()
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['content-type'] == 'application/json;charset=UTF-8'

for actualBook in json_response:
    if actualBook['isbn'] == 'RS244':
        print(actualBook)
        break


exBook = {
             "book_name": "Learn Appium Automation with Java",
              "isbn": "RS244",
              "aisle": "2223"
        }
assert actualBook == exBook




