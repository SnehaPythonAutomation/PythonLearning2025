import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/1034", )
print(response_body.text)
print(response_body.headers)

#Verify ?
# Assertion : verify expected result with actual result
# Status code ER -> 200
# AR-> 200
#
# if id =1035 ER-> 404
#     AR-> 404

