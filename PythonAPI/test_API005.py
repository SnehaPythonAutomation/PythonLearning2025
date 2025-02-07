# Assertion - assert
# But for Assertion will use PyTest Library
# PyTest - name should be start with test eg.., test_API005
# Dont have to create main function in it.

import pytest
import requests

def test_sample1():
    assert 4 == 4


def test_sample2():
    assert 5 == 6

def test_getrequest():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/384", )
    assert response_body.status_code == 200  # If sc !=200 it error, else it will not give error
    data = response_body.json()

    # Assertions

    assert 'firstname' in data, "Incorrect firstName"
    assert 'lastname' in data, "LastName key is present "

    assert data["firstname"] == "Joh", "Incorrect FirstName Jim"
    assert data["lastname"] == "Smith", "Incorrect LastName"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Check-in date"
    assert data["bookingdates"]["checkout"] == "2019-01-01", "Incorrect Check-out date"