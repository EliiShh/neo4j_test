from flask import Blueprint, request, jsonify
from app.service.device_service import insert_devices_service, count_devices_connected_service, direct_connection_exists_service, most_recent_interaction_service


device_blueprint = Blueprint("phone", __name__)



@device_blueprint.route('/api/connected_count/<string:device_id>', methods=['GET'])
def count_devices_connected(device_id):
    try:
        res = count_devices_connected_service(device_id)
        return jsonify(res), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501


@device_blueprint.route('/api/direct_connection', methods=['GET'])
def direct_connection_exists():
    try:
        from_device_id = request.args.get('from_device_id')
        to_device_id = request.args.get('to_device_id')
        res = direct_connection_exists_service(from_device_id, to_device_id)
        return jsonify(res), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501

@device_blueprint.route('/api/most_recent_interaction/<string:device_id>', methods=['GET'])
def most_recent_interaction(device_id):
    try:
        data = most_recent_interaction_service(device_id)
        return jsonify(data), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501