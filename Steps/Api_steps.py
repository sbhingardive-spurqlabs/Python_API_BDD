from behave import *

use_step_matcher("parse")



# use_step_matcher("re")
from Features.Utils.API_Utility import API_Utility

api_util = API_Utility()



@when('User sends "{method}" call to endpoint "{endpoint}"')
def step_impl(context,method, endpoint):
    global response
    response = api_util.Method_Call(context.table,method, endpoint)
    # print(response.status_code)
    # print(response.json())



@then('User verifies the status code is "{status_code}"')
def step_impl(context,status_code):
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)



@step("User verifies response contains following information")
def step_impl(context):
    api_util.Verify_GET(context.table)
    response_body = response.json()
    print(response_body)

    assert response_body['data']['first_name'] == context.table[0][0]
    assert response_body['data']['last_name'] == context.table[0][1]
    assert response_body['data']['email'] == context.table[0][2]


@step("User verifies response body contains following information")
def step_impl(context):
    api_util.Verify_POST(context.table)
    response_body = response.json()
    print(response_body)

    assert response_body['name'] == context.table[0][0]
    assert response_body['job'] == context.table[0][1]
