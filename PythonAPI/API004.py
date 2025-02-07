import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1034", )
    assert response_body.status_code == 200  # If sc !=200 it error, else it will not give error
    data = response_body.json()

    # Assertions

    assert 'firstname' in data, "Incorrect firstName"
    assert 'lastname' in data, "LastName key is present "

    assert data["firstname"] == "Joh", "Incorrect FirstName Jim"
    assert data["lastname"] == "Smith", "Incorrect LastName"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Check-in date"
    assert data["bookingdates"]["checkout"] == "2019-01-01", "Incorrect Check-out date"

if __name__ == '__main__':
    main()
