import pytest
import requests
import json


def test_sample():
    assert 4 == 4


def test_sample2():
    assert 5 == 5


def test_getrequest():
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
    assert data["bookingdates"]["Check-in"] == "2018-01-01", "Incorrect Message"
