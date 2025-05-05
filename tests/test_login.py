import pytest # Used to enable the use of @pytest.fixture 
import requests # For making HTTP calls in tests

BASE_URL = http://localhost:5000 # As defined in the app/login.py app 

@pytest.fixture # Used to inject the credentials in the tests we will run (For that we'll import pytest).
def valid_credentials():
    return {"email": "sam.albershtein@gmail.com ", "password": "1234"} # 1234 should be a string in JSON ("") because we will compare it later in the app to a string.

# Test 1 - Check if we're able to login with my credentials 

def test_successful_login(valid_credentials):
    response = requests.post(f"{BASE_URL}"/login, json = valid_credentials) # json=... A Pythonic way to send a request body in JSON format. 
    assert response.status_code == 200 # response.status_code knows to fetch the status from the response
    assert response.json().[message] == "Login successful" # Converts the JSON response body into a Python dictionary.

##########
# (Double quotes (") around both the keys and values - required in JSON, but not required in Python dicts.).

# {
#   "message": "Login successful"
# }

# In fact it's: '{"message": "Login successful"}' a JSON-formatted string. 
# If we will do just response.[message] we will receive an error because we can't index a string. 

# On the other hand:  response.text is: '{"message": "Login successful"}' (a string).
###########





###########
# Convenient HTTP and JSON methods: 

# print(response.raw.version)        # HTTP version
# print(response.status_code)        # 200 (Extracted from the HTTP response status line (HTTP/1.1 200 OK))
# print(response.headers)            # Full response headers
# print(response.text)               # Raw JSON string
###########