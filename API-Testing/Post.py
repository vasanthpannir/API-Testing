import requests
import json
from payload import *

addbook_response = requests.post('http://216.10.245.166/Library/Addbook.php',
                                 json=addpayload("1223")
                                 , headers={"Content-Type": "application/json"},
                                 )

print(addbook_response.json())
response_json = addbook_response.json()
print(type(response_json))
bookId = response_json['ID']
print(bookId)

# Delete Book


response_delete = requests.delete('http://216.10.245.166/Library/DeleteBook.php', json=
{"ID": bookId},
                                headers={"Content-Type": "application/json"}
                                )

print("Delete Response Status Code:", response_delete.status_code)
print("Delete Response Body:", response_delete.json())


