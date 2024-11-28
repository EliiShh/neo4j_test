from flask import jsonify, Blueprint

from app.service.interaction_service import devices_stronger_signal_service, devices_connected_bluetooth_service

interaction_blueprint = Blueprint('interaction', __name__)



@interaction_blueprint.route('/api/bluetooth_path', methods=['GET'])
def find_all_devices_connected_bluetooth():
    try:
        data = devices_connected_bluetooth_service()
        return jsonify(data), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501

@interaction_blueprint.route('/api/stronger_signal/<signal_strength>', methods=['GET'])
def find_devices_stronger_signal(signal_strength):
    try:
        data = devices_stronger_signal_service(int(signal_strength))
        return jsonify(data), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501


