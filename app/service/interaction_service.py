from app.db.models import Interaction
from app.repo.interaction_repo import create_interaction, find_all_devices_connected_bluetooth, \
    find_devices_stronger_signal


def insert_interaction_service(interaction: dict):
    interaction_to_neo = Interaction(**interaction)
    status = create_interaction(interaction_to_neo)
    return {"status": status}

def devices_connected_bluetooth_service():
    res = find_all_devices_connected_bluetooth()[0]
    return {"cunt": len(res["path"]), "all_res": res}


def devices_stronger_signal_service(signal_strength: int):
    res = find_devices_stronger_signal(signal_strength)
    return {"cunt": len(res), "devices_relationship": res}

