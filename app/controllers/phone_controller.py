from flask import Blueprint, request, jsonify
from app.service.interaction_service import insert_interaction
from app.service.phone_service import insert_devices


phone_blueprint = Blueprint("phone", __name__)




@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   data = request.get_json()
   res_devices = insert_devices(data["devices"])
   res_interaction = insert_interaction(data["interaction"])
   return jsonify({"devices": res_devices, "interaction": res_interaction}), 201



# MATCH (start:Device)
# MATCH (end:Device)
# WHERE start <> end
# MATCH path = shortestPath((start)-[:INTERACTED_WITH*]->(end))
# WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
# WITH path, length(path) as pathLength
# ORDER BY pathLength DESC
# LIMIT 1
# RETURN path
#





# device_blueprint = Blueprint('device', __name__)
#
# @device_blueprint.route('/api/devices', methods=['POST'])
# def create_device():
#     data = request.get_json()
#     location = data.pop('location')
#     device = Device(**data, location=Location(**location))
#     DeviceRepository.create_device(device)
#     return jsonify({'message': 'Device created successfully'}), 200
#
# @device_blueprint.route('/api/bluetooth_path', methods=['GET'])
# def find_all_devices_connected_bluetooth():
#     db = get_db()
#     with db.session() as session:
#         data = DeviceRepository.find_all_devices_connected_bluetooth(session)
#     return jsonify(data), 200
#
# @device_blueprint.route('/api/stronger_signal/<int:signal_strength>', methods=['GET'])
# def find_devices_stronger_signal(signal_strength):
#     db = get_db()
#     with db.session() as session:
#         data = DeviceRepository.find_devices_stronger_signal(session, signal_strength)
#     return jsonify(data), 200
#
# @device_blueprint.route('/api/connected_count/<string:device_id>', methods=['GET'])
# def count_devices_connected(device_id):
#     db = get_db()
#     with db.session() as session:
#         count = DeviceRepository.count_devices_connected(session, device_id)
#     return jsonify({'count': count}), 200
#
# @device_blueprint.route('/api/direct_connection', methods=['GET'])
# def direct_connection_exists():
#     from_device_id = request.args.get('from_device_id')
#     to_device_id = request.args.get('to_device_id')
#     db = get_db()
#     with db.session() as session:
#         exists = DeviceRepository.direct_connection_exists(session, from_device_id, to_device_id)
#     return jsonify({'exists': exists}), 200
#
# @device_blueprint.route('/api/most_recent_interaction/<string:device_id>', methods=['GET'])
# def most_recent_interaction(device_id):
#     db = get_db()
#     with db.session() as session:
#         data = DeviceRepository.most_recent_interaction(session, device_id)
#     return jsonify(data), 200
