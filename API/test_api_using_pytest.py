'''
Create 2 TC which invoke setup cleanup. Setup should return user_id
Setup:(reusable setup or all tests)
 
  - Create a User
	POST https://reqres.in/api/users
	request body:  {"name": "morpheus", "job": "leader"}
	Response: {"id": "2", "createdAt": "<<date>>"}
 
 
Test1:
       Use the user id that was generated in the setup and get the user id using below GET request and validate it returns the same user id.
	GET https://reqres.in/api/users/2
 
 
Test2:
	Update the user using below request.
	PUT https://reqres.in/api/users/2
	request body: {"name": "morpheus", "job": "zion resident"}
 
 
Cleanup:
	Remove the user using below request.
	DELETE https://reqres.in/api/users/2 
 pytest -s -v test_api_using_pytest.py 
 '''

import pytest
import requests
import json

@pytest.fixture # Default function scope
def setup_user():
    # Setup: Create a user
    url = "https://reqres.in/api/users"
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(url, data=json.dumps(payload))
    user_data = response.json()
    yield user_data['id']  # Return the user id
    # Cleanup: Remove the user
    delete_url = f"{url}/{user_data['id']}"
    requests.delete(delete_url)

def test_get_user(setup_user):
    # Test 1: Get the user using the user id generated in setup
    user_id = setup_user
    url = f"https://reqres.in/api/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id

def test_update_user(setup_user):
    # Test 2: Update the user using the user id generated in setup
    user_id = setup_user
    url = f"https://reqres.in/api/users/{user_id}"
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put(url, data=json.dumps(payload))
    assert response.status_code == 200
    assert response.json()['updatedAt'] is not None
