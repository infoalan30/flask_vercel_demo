from flask import Flask, jsonify, request

app = Flask(__name__)

data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

@app.route('/get_age', methods=['GET'])
def get_age():
    name = request.args.get('name')
    if name in data_store:
        age = data_store[name]
        response_data = {
            "status": "success",
            "name": name,
            "age": age
        }
    else:
        response_data = {
            "status": "error",
            "message": "Name not found"
        }
    return jsonify(response_data)

def handler(request):
    environ = request.environ
    response = app(environ, start_response)
    status, headers = start_response.status, start_response.headers
    body = b''.join(response)
    return {
        "statusCode": int(status.split()[0]),
        "headers": dict(headers),
        "body": body.decode('utf-8')
    }

class StartResponse:
    def __init__(self):
        self.status = "200 OK"
        self.headers = []

    def __call__(self, status, headers):
        self.status = status
        self.headers = headers
        return lambda *args: None

start_response = StartResponse()
