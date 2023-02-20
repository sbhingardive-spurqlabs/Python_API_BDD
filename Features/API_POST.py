# import requests
# import json
#
# api_url = "https://reqres.in/"
# endpoint_url = "api/users/2"
# uri = api_url + endpoint_url
#
# payload ={
#     "name": "James",
#     "job": "leader"
# }
#
#
#
# response = requests.request("POST", uri,data = payload)
# print(response.status_code)
# response_body = response.json()
# if(response.status_code == 201):
#     print("Pass")
# else:
#     print("Fail")
# print(response_body)