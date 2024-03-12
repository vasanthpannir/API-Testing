import  requests
from utilities.configuration import *
import json


session = requests.session()
login_page_response = session.get('https://github.com/user')
cookies = login_page_response.cookies
url = "https://github.com/user"
login_github = requests.post(url,auth=('bmsmnti.123@gmail.com',getpassword()),cookies=cookies)
print(login_github.status_code)
print(login_github.text)



