from urllib.parse import parse_qs
import json

data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

def handler(request):
    # 解析查询参数
    query = parse_qs(request.environ['QUERY_STRING'])
    name = query.get('name', [None])[0]

    # 逻辑处理
    if name in data_store:
        response_data = {
            "status": "success",
            "name": name,
            "age": data_store[name]
        }
    else:
        response_data = {
            "status": "error",
            "message": "Name not found"
        }

    # 返回 Vercel 期望的格式
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response_data)
    }
