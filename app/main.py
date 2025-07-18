from flask import Flask, request, jsonify

# jsonify turns Python dict into JSON
# request is used to to analyze http requests and response + parse the http request as a python dict.


VALID_EMAIL = "sam.albershtein@gmail.com"
VALID_PASSWORD = "1234"


def create_app():
    app = Flask(__name__)

    @app.route("/login", methods=["POST"])
    def login():
        data = (
            request.json
        )  # Parses the request and returns it as a python dict. (.json is not a function but a property - a property that triggers flasks logic under the hood json.load )

        if not data:
            return (
                jsonify({"error": "No data provided"}),
                400,
            )  # Jsonify returns the dictionary as a json format and include 400 in the http response.

        # 400 is the HTTP status code for "Bad Request" - indicates that the server cannot process the request due to a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

        email = data.get(
            "email"
        )  # Using .get() avoids crashes and lets handle errors gracefully (returns None), unlike data["email"] (If it's not there we get a crash)
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Missing fields"}), 400

        if email == VALID_EMAIL and password == VALID_PASSWORD:
            return jsonify({"message": "Login successful"}), 200

        # 200 is the HTTP status code for "OK" - indicates that the request has succeeded.

        else:
            return jsonify({"error": "Invalid credentials"}), 401

        # 401 is the HTTP status code for "Unauthorized" - indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5001)

##########
# The above code is a simple Flask application that provides a login endpoint.

# The jsonify function is used to construct the HTTP response in JSON format.
# Thanks to jsonify the content type is set to: application/json.


#   HTTP/1.1 200 OK
#   Content-Type: application/json
#   Content-Length: 34
#   Server: Werkzeug/2.0.3 Python/3.9.5
#   Date: Mon, 06 May 2025 15:15:00 GMT

#   {
#     "message": "Login successful"
#   }
#
##########
