import pytest # Used to enable the use of @pytest.fixture 
import requests # For making HTTP calls in tests

BASE_URL = "http://app:5001" # As defined in the app/login.py app (Changed to app because that's how the hostname of the flask service is defined in the docker compose)



@pytest.fixture # Used to inject the credentials in the tests we will run (For that we'll import pytest).
def valid_credentials():
    return {"email": "sam.albershtein@gmail.com", "password": "1234"} # 1234 should be a string in JSON ("") because we will compare it later in the app to a string.



# Test 1 - Check if we're able to login with my credentials 

def test_successful_login(valid_credentials):
    response = requests.post(f"{BASE_URL}/login", json = valid_credentials) # json=... A Pythonic way to send a request body in JSON format. 
    # We're not getting back a string or raw data — We get a Response object from the requests library.
    assert response.status_code == 200 # response.status_code knows to fetch the status from the response. 
    assert response.json()["message"] == "Login successful" # Converts the JSON response body into a Python dictionary.



# Test 2 - Check if we're able to login with invalid credentials

def test_invalid_credentials():
    credentials = {"email": "notsam@gmail.com", "password": "123"}
    response = requests.post(f"{BASE_URL}/login", json = credentials)
    assert response.status_code == 401 
    assert response.json()["error"] == "Invalid credentials" 



# Test 3 - Check if we're able to login without credentials

def test_missing_credentials():
    credentials = {"email": "notsam@gmail.com"}
    response = requests.post(f"{BASE_URL}/login", json = credentials)
    assert response.status_code == 400 
    assert response.json()["error"] == "Missing fields"



# Test 4 - Check if we're able to login without sending json payload 

def test_missing_payload():
    response = requests.post(f"{BASE_URL}/login", json = {})
    assert response.status_code == 400
    assert response.json()["error"] == "No data provided" 
    # Can also use below properties like that: assert "Invalid credentials" in response.text


###########
# Convenient HTTP and JSON Properties:
# Here we get back a Response object, and we can access various parts of the HTTP response.

# Unlike a method that performs work — it doesn’t just return stored data.
# Property - Like asking someone their age: "How old are you?" → "25" (A property was defined in the class requests.models.Response)
# Properties are defined in the backend, usually inside the class, and give the clean experience of .status_code, .headers 

# class Response:
#     @property
#     def status_code(self):
#         return self._status_code

# Method - Like asking someone to do something: "Can you calculate this for me?" → [Does work]

# print(response.raw.version)        # HTTP version
# print(response.status_code)        # 200 (Extracted from the HTTP response status line (HTTP/1.1 200 OK))
# print(response.headers)            # Full response headers
# print(response.text)               # Raw JSON string
###########

##########
# (Double quotes (") around both the keys and values - required in JSON, but not required in Python dicts.).

# {
#   "message": "Login successful"
# }

# In fact it's: '{"message": "Login successful"}' a JSON-formatted string. 
# If we will do just response.[message] we will receive an error because we can't index a string. 

# On the other hand:  response.text is: '{"message": "Login successful"}' (a string).
###########
