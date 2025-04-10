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

# Vercel Serverless 入口
def handler(req):
    from wsgiref.simple_server import make_server
    # 将请求交给 Flask 处理
    response = app.wsgi_app(req.environ, start_response)
    status, headers = start_response.status, start_response.headers
    return {
        "statusCode": int(status.split()[0]),
        "headers": dict(headers),
        "body": "".join(response)
    }

# WSGI 响应处理
class StartResponse:
    def __init__(self):
        self.status = None
        self.headers = []

    def __call__(self, status, headers):
        self.status = status
        self.headers = headers
        return self

start_response = StartResponse()
