from flask import Flask, jsonify, request

# IMPORTANT: The Flask app object MUST be named 'app' for Vercel's default detection,
# OR you configure Vercel specifically to find it if named differently.
# We'll stick with 'app'.
app = Flask(__name__)

# 示例数据 (Your example data)
data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

# Your API route - no changes needed here
@app.route('/get_age', methods=['GET'])
def get_age():
    # Get the 'name' query parameter from the URL (e.g., /api/get_age?name=Alice)
    name = request.args.get('name')

    if name and name in data_store: # Check if name exists and is in our data
        age = data_store[name]
        response_data = {
            "status": "success",
            "name": name,
            "age": age
        }
        # Return JSON response with HTTP status code 200 (OK)
        return jsonify(response_data), 200
    elif name: # Name was provided but not found
         response_data = {
            "status": "error",
            "message": f"Name '{name}' not found"
        }
         # Return JSON response with HTTP status code 404 (Not Found)
         return jsonify(response_data), 404
    else: # No 'name' query parameter was provided
        response_data = {
            "status": "error",
            "message": "Missing 'name' query parameter"
        }
        # Return JSON response with HTTP status code 400 (Bad Request)
        return jsonify(response_data), 400

# Add a simple root route for basic testing (optional)
@app.route('/', methods=['GET'])
def home():
    # This will map to /api/ if you deploy like this
    return jsonify({"message": "Welcome to the Age API! Use /api/get_age?name=<name>"})

# --- IMPORTANT ---
# REMOVE or COMMENT OUT the following lines:
# if __name__ == '__main__':
#     app.run(debug=True)
# Vercel handles the server part, you just provide the 'app' object.
