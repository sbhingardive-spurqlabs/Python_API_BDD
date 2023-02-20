# import requests
# import json
#
# api_url = "https://reqres.in/"
# endpoint_url = "api/users/2"
# uri = api_url + endpoint_url
#
# response = requests.request("GET", uri)
# print(response.status_code)
# response_body = response.json()
#
#
# if(response.status_code == 200):
#     print("Pass")
# else:
#     print("Fail")
#
# print(response_body['data']['id'])
# print(response_body['data']['first_name'])
# print(response.apparent_encoding)
# print(response.content)
# print(response.headers)