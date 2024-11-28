from app.db.models.device import Device, Location
from app.repo.phone_repo import create_device


def insert_data(data: dict):
    devices = [Device(**d, location=Location(**d["location"])) for d in data["devices"]]
    if devices[0].device_id == devices[1].device_id:
        return {"error": "the devices them equal"}
    [create_device(device) for device in devices]








{'devices':
     [{'id': 'aebf8705-ee7f-4508-96bd-cfc513c2aba4',
       'name': 'Anthony', 'brand': 'Ford and Sons',
       'model': 'Spend Return',
       'os': 'InternationalOS 14.3',
       'location': {'latitude': -54.667791,
                    'longitude': 127.672628,
                    'altitude_meters': 3818,
                    'accuracy_meters': 4}
       },
      {'id': 'aee32a7c-b725-4812-84e3-446694253c75',
       'name': 'Lisa', 'brand': 'Robles-Morrow',
       'model': 'Within Ever',
       'os': 'ReturnOS 14.8',
       'location': {'latitude': 89.4800265,
                    'longitude': 134.910672,
                    'altitude_meters': 1138,
                    'accuracy_meters': 5}
       }
     ],
 'interaction': {'from_device': 'aebf8705-ee7f-4508-96bd-cfc513c2aba4',
                 'to_device': 'aee32a7c-b725-4812-84e3-446694253c75',
                 'method': 'NFC', 'bluetooth_version': '4.3',
                 'signal_strength_dbm': -40,
                 'distance_meters': 14.48,
                 'duration_seconds': 121,
                 'timestamp': '2019-09-11T20:11:58'}
}