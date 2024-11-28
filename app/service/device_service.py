from app.db.models import Device, Location, Interaction
from app.repo.device_repo import create_device, direct_connection_exists, count_devices_connected, \
    most_recent_interaction


def insert_devices_service(devices: list):
    devices = [Device(**{**d, "location": Location(**d["location"])}) for d in devices]

    if devices[0].id == devices[1].id:
        return {"error": "the devices them equal"}
    ids= [create_device(device) for device in devices]
    return {"status": f"add {ids}"}


def direct_connection_exists_service(from_device_id: str, to_device_id: str):
    res = direct_connection_exists(from_device_id, to_device_id)
    return {"if_connection": res > 0}


def count_devices_connected_service(device_id: str):
    res = count_devices_connected(device_id)
    return {"count_devices_connected": res}


def most_recent_interaction_service(device_id: str):
    result = most_recent_interaction(device_id)
    other_node = result["other"]
    relationship = result["r"]
    node_dict = {
        "element_id": other_node.element_id,
        "labels": list(other_node.labels),
        "properties": dict(other_node)
    }
    relationship_dict = dict(relationship)
    return {
        "node": node_dict,
        "relationship": relationship_dict
    }

