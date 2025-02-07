import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1034", )
    assert response_body.status_code == 200  # If sc !=200 it error, else it will not give error


if __name__ == '__main__':
    main()
