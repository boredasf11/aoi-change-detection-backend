from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/process_aoi", methods=["POST"])
def process_aoi():
    data = request.get_json()

    # Placeholder satellite image (demo)
    sample_image_url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/144000/144321/world.topo.bathy.200412.3x21600x10800.jpg"

    return jsonify({
        "status": "success",
        "message": "AOI received and processed.",
        "image_url": sample_image_url
    })

if __name__ == "__main__":
    app.run()
