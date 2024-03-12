import requests
import json


def main():
    id = '1421'
    url = 'https://restful-booker.herokuapp.com/booking/'
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200
    data = response_body.json()
    assert 'firstname' in data, "Incorrect firstname"
    assert 'lastname' in data, "Incorrect lastname"

    assert data["firstname"] == "Josh", "FirstName is Amit"
    assert data["lastname"] == "Allen", "LastName is Amit"
    assert data["bookingdates"]["Checkin"] == "2018-01-01", "Incorrect Message"

if __name__ == '__main__':
    main()
