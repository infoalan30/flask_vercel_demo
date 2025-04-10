from flask import Flask, jsonify, request
import logging # Optional: Add logging for debugging Vercel requests

app = Flask(__name__)

# Optional: Configure logging to see requests in Vercel logs
logging.basicConfig(level=logging.INFO)

# 示例数据 (Your example data)
data_store = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "David": 28,
    "Eva": 22
}

# Add a handler to log incoming request paths (useful for debugging)
@app.before_request
def log_request_info():
    app.logger.info('Request Path: %s', request.path)
    app.logger.info('Request Args: %s', request.args)


# --- CHANGE HERE: Add /api prefix ---
@app.route('/api/get_age', methods=['GET'])
def get_age():
    app.logger.info('Accessed /api/get_age route') # Log access
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

# --- CHANGE HERE: Add /api prefix ---
# This route will now match requests to https://<your-url>/api/
@app.route('/api/', methods=['GET'])
def api_home():
    app.logger.info('Accessed /api/ route') # Log access
    # This will map to /api/
    return jsonify({"message": "Welcome to the Age API! Use /api/get_age?name=<name>"})

# --- Optional: Add a root route just for base domain testing ---
# This will respond if someone hits https://<your-url>/ directly,
# but it might require separate routing in vercel.json if you want it
# alongside the /api routes handled by index.py
@app.route('/', methods=['GET'])
def root_home():
    app.logger.info('Accessed / route') # Log access
    return jsonify({"message": "API is available under /api/"})


# IMPORTANT: Ensure this part is REMOVED or COMMENTED OUT
# if __name__ == '__main__':
#     app.run(debug=True)
