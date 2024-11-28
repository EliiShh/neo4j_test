from app.db.database import driver

def create_device(device):
    with driver.session() as session:
        query = (
            "MERGE (d:Device {id: $id}) "
            "SET d.name = $name, d.brand = $brand, d.model = $model, d.os = $os, "
            "d.latitude = $latitude, d.longitude = $longitude, "
            "d.altitude_meters = $altitude_meters, d.accuracy_meters = $accuracy_meters"
        )
        params = {"id":device.id, "name":device.name, "brand":device.brand,
                    "model":device.model, "os":device.os, "latitude":device.location.latitude,
                    "longitude":device.location.longitude, "altitude_meters":device.location.altitude_meters,
                    "accuracy_meters":device.location.accuracy_meters}
        session.run(query, params).single()
        return device.id





def direct_connection_exists(from_device_id: str, to_device_id: str):
    with driver.session() as session:
        query = (
            "MATCH (from:Device {id: $from_device_id})-[:CONNECTED]-(to:Device {id: $to_device_id}) "
            "RETURN count(*) as count"
        )
        result = session.run(query, from_device_id=from_device_id, to_device_id=to_device_id).single()
        return result["count"] > 0



def count_devices_connected(device_id: str):
    with driver.session() as session:
        query = (
            "MATCH (:Device {id: $device_id})-[:CONNECTED]-(:Device) "
            "RETURN count(*) as count"
        )
        result = session.run(query, device_id=device_id).single()
        return result["count"]


def most_recent_interaction(device_id: str):
    with driver.session() as session:
        query = (
            "MATCH (d:Device {id: $device_id})-[r:CONNECTED]->(other:Device) "
            "RETURN r, other ORDER BY r.timestamp DESC LIMIT 1"
        )
        return session.run(query, device_id=device_id).single()


