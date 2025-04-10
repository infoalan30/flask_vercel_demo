from flask import Flask, jsonify, request

# 创建 Flask 应用
app = Flask(__name__)

# 示例数据
data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

# 定义路由
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

# Vercel 的 Serverless 函数入口
def handler(req):
    # 将 WSGI 请求传递给 Flask 应用
    return app(req.environ, start_response)

# WSGI 的 start_response 模拟函数
def start_response(status, headers):
    # Vercel 会处理状态码和头部，这里仅占位
    pass