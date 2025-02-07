# API
# Request Lib

# we need Requests Library to make a CURD opration/ To make a HTTP methods(Get, Put , Post, Delete, Patch)

import requests


def main():  # main function
    # get- URL
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1034", )
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code == 200 :
        print("TC#1- GET request is successfully")
    else:
        print("TC2#- GET request is not successfully")

# To make API Testing request
# URL, auth, headers, cookies, data(payload), json, file

# what we need to validate in API
# response, headers, statuscode, responsetime, JSON schema validation

if __name__ == "__main__":
    main()
