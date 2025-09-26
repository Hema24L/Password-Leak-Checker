from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import hashlib
import requests

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)

# app.static_folder points to your React build
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/check-leak', methods=['POST'])
def check_leak():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    password = data.get("password")
    if not password:
        return jsonify({"error": "Password is required"}), 400

    sha1_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_pass[:5], sha1_pass[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "HIBP API error"}), 500

    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h.strip().upper() == suffix:
            return jsonify({
                "status": "leaked",
                "count": int(count),
                "message": f"⚠️ Found {count} times in leaks!"
            })
    return jsonify({
        "status": "safe",
        "count": 0,
        "message": "✅ Not found in known leaks."
    })

# Catch all for React routing
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
