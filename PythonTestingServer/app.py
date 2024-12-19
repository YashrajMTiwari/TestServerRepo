from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for testing
buoy_data = {
    "BUOY1234": {"latitude": 36.7783, "longitude": -119.4179},
    "BUOY5678": {"latitude": 37.7749, "longitude": -122.4194},
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
