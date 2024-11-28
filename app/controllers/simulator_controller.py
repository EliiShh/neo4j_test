from flask import Blueprint, request, jsonify
from app.service.interaction_service import insert_interaction_service
from app.service.device_service import insert_devices_service


simulator_blueprint = Blueprint("simulator", __name__)


@simulator_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   try:
      data = request.get_json()
      res_devices = insert_devices_service(data["devices"])
      res_interaction = insert_interaction_service(data["interaction"])
      return jsonify({"devices": res_devices, "interaction": res_interaction}), 201
   except Exception as e:
      error = str(e)
      print(error)
      return jsonify({'error': error}), 501