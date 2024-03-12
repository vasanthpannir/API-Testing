import requests
import json

addbook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json={
    "name": "Learn Appium Automation with Java",
    "isbn": "bcd",
    "aisle": "227",
    "author": "John foe"
}, headers={"Content-Type": "application/json"})

# Check the status code
print("Status Code:", addbook_response.status_code)

# Print the raw response text
print("Response Text:", addbook_response.text)

# Attempt to parse JSON only if the response indicates success
if addbook_response.ok:
    try:
        print(addbook_response.json())
    except json.JSONDecodeError:
        print("Failed to decode JSON")
else:
    print("Request failed.")