from app.db.database import driver
from app.db.models import Interaction


def create_interaction(interaction: Interaction):
    with driver.session() as session:
        query = (
            "MATCH (from:Device {id: $from_device}), (to:Device {id: $to_device}) "
            "CREATE (from)-[r:CONNECTED {method: $method, bluetooth_version: $bluetooth_version, "
            "signal_strength_dbm: $signal_strength_dbm, distance_meters: $distance_meters, "
            "duration_seconds: $duration_seconds, timestamp: $timestamp}]->(to)"
        )
        session.run(query, from_device=interaction.from_device, to_device=interaction.to_device,
                    method=interaction.method, bluetooth_version=interaction.bluetooth_version,
                    signal_strength_dbm=interaction.signal_strength_dbm, distance_meters=interaction.distance_meters,
                    duration_seconds=interaction.duration_seconds, timestamp=interaction.timestamp)
        return "created"
