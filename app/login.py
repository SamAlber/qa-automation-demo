from flask import Flask, request, jsonify 
# jsonify turns Python dict into JSON
# request is used to to analyze http requests and response + parse the http request as a python dict. 

app = Flask(__name__)

VALID_EMAIL = "sam.albershtein@gmail.com"
VALID_PASSWORD = "1234"

@app.route("/login", methods=["POST"])
def login():
    data = request.json # Parses the request and returns it as a python dict. (.json is not a function but a property - a property that triggers flasks logic under the hood json.load )

    if not data:
        return jsonify({"error": "No data provided"}), 400 # Jsonify returns the dictionary as a json format and include 400 in the http response

    email = data.get("email") # Using .get() avoids crashes and lets handle errors gracefully (returns None), unlike data["email"] (If it's not there we get a crash)
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    if email == VALID_EMAIL and password == VALID_PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
