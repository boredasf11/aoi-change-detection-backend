from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/process_aoi", methods=["POST"])
def process_aoi():
    data = request.get_json()
    return jsonify({"status": "received", "aoi": data})

if __name__ == "__main__":
    app.run()
