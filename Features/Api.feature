# Created by hp at 31-01-2023
Feature: API demo 1


    @api
Scenario: Verify GET call for single user
	When User sends "GET" call to endpoint "api/users/2"
	Then User verifies the status code is "200"
	And User verifies response contains following information
	| First_name | Last_name | Mail-id                |
	| Janet      | Weaver    | janet.weaver@reqres.in |

	@api
	Scenario: Verify POST call for single user
	When User sends "POST" call to endpoint "api/users"
	| Name     | Job    |
	| Morpheus | Leader |
	Then User verifies the status code is "201"
	And User verifies response body contains following information
	| Name     | Job    |
	| Morpheus | Leader |