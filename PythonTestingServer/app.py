from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for testing
buoy_data = {
    "BUOY1234": {"latitude": 38.9072, "longitude": -77.0369},
    "BUOY5678": {"latitude": 35.6762, "longitude": 139.6503},
    "BUOY9898": {"latitude": 28.6139, "longitude": 77.2090},
    "BUOY7876": {"latitude":  -66.00016, "longitude": -60.44025},
}

@app.route('/api/location', methods=['GET'])
def get_location():
    device_id = request.args.get('device_id')
    if device_id in buoy_data:
        return jsonify({
            "device_id": device_id,
            "latitude": buoy_data[device_id]["latitude"],
            "longitude": buoy_data[device_id]["longitude"],
        })
    return jsonify({"error": "Device not found"}), 404

if __name__ == '__main__':
    app.run()
