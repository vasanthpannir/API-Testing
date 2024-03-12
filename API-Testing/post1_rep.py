import requests
from payload import *
from utilities.resource import *
from utilities.configuration import *

url = getconfig()['API']['endpoint']+ Addapi.addbook
url2 = getconfig()['API']['endpoint']+ Addapi.delbool1

headers={"Content-Type": "application/json"}

addbook_response = requests.post(url, json=addBookPayload("dvve3"), headers=headers, )

config = getconfig()
print(config)  # Print entire config
print(config['API'])  # Print API section

print(addbook_response.status_code)
print(addbook_response.json())
response_json = addbook_response.json()
print(type(response_json))
bookId = response_json['ID']
print(bookId)

delbook_response = requests.post(url2, json={"ID": bookId}, headers=headers,)

assert delbook_response.status_code == 200
print(delbook_response.json())
