from app.db.models import Device, Location, Interaction
from app.repo.phone_repo import create_device


def insert_devices(devices: list):
    devices = [Device(**{**d, "location": Location(**d["location"])}) for d in devices]

    if devices[0].id == devices[1].id:
        return {"error": "the devices them equal"}
    ids= [create_device(device) for device in devices]

    return {"status": f"add {ids}"}


data = {'devices': [
    {'id': '3e269103-04d7-4da8-b07c-add259921744', 'name': 'Jackson', 'brand': 'Jenkins, Davis and Patton',
     'model': 'Hear Product', 'os': 'KeepOS 6.5',
     'location': {'latitude': 74.43674, 'longitude': 166.944776, 'altitude_meters': 2560, 'accuracy_meters': 46}},
    {'id': 'd4c05640-83f7-4a8d-a924-5ec8d3b058c8', 'name': 'Kelly', 'brand': 'Curry LLC', 'model': 'During Already',
     'os': 'EverOS 8.7',
     'location': {'latitude': 12.0805925, 'longitude': 72.762496, 'altitude_meters': 4140, 'accuracy_meters': 8}}],
       'interaction': {'from_device': '3e269103-04d7-4da8-b07c-add259921744',
                       'to_device': 'd4c05640-83f7-4a8d-a924-5ec8d3b058c8', 'method': 'WiFi',
                       'bluetooth_version': '5.3', 'signal_strength_dbm': -54, 'distance_meters': 14.31,
                       'duration_seconds': 184, 'timestamp': '2018-05-07T17:44:04'}}

