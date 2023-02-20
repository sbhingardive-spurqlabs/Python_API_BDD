import json
import requests


class API_Utility:

    data = json.load(open("Resources/config.json"))
    api_url = data["API_URL"]
    global response

    def Method_Call(self,table, method, endpoint):
        if method == 'GET':
            uri = self.api_url + endpoint
            response = requests.request("GET",uri)
            return response
        if method == 'POST':
            uri = self.api_url + endpoint
            payload = {
                "name": table[0][0],
                "job": table[0][1]
            }
            response = requests.request("POST", uri, data=payload)
            return response

    def Get_Status_Code(self):
        status_code = response.status_code
        return status_code

    def Verify_GET(self,table):
        for row in table:
            first_name = row['First_name']
            last_name = row['Last_name']
            email = row['Mail-id']
            return first_name, last_name, email

    def Verify_POST(self,table):
        for row in table:
            name = row['Name']
            job = row['Job']
            return name, job




    #
    # def POST_Call(self, endpoint):
    #     uri = self.api_url + endpoint
    #     payload = {
    #         "name": "James",
    #         "job": "leader"
    #     }
    #     response = requests.request("POST", uri, data=payload)
    #     return response
    #
    # def Status_Code_Verify(self,status_code, n):
    #     if n == "GET":
    #         actual_code = 200
    #         if (status_code == actual_code):
    #             print('Pass')
    #         else:
    #             print('Fail')
    #     if n == "POST":
    #         actual_code = 201
    #         if (status_code == actual_code):
    #             print('Pass')
    #         else:
    #             print('Fail')
    #
