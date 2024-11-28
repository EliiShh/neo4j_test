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

def find_all_devices_connected_bluetooth():
    with driver.session() as session:
        query = (
            "MATCH (d1:Device)-[r:CONNECTED {method: 'Bluetooth'}]->(d2:Device) "
            "RETURN d1, r, d2"
        )
        return session.run(query).data()


print(find_all_devices_connected_bluetooth())

# def find_devices_stronger_signal(session: Session, signal_strength: int):
#     query = (
#         "MATCH (d1:Device)-[r:CONNECTED]->(d2:Device) "
#         "WHERE r.signal_strength_dbm > $signal_strength "
#         "RETURN d1, r, d2"
#     )
#     return session.run(query, signal_strength=signal_strength).data()
#
# def count_devices_connected(session: Session, device_id: str):
#     query = (
#         "MATCH (:Device {device_id: $device_id})-[:CONNECTED]-(:Device) "
#         "RETURN count(*) as count"
#     )
#     result = session.run(query, device_id=device_id).single()
#     return result["count"]
#
# def direct_connection_exists(session: Session, from_device_id: str, to_device_id: str):
#     query = (
#         "MATCH (from:Device {device_id: $from_device_id})-[:CONNECTED]-(to:Device {device_id: $to_device_id}) "
#         "RETURN count(*) as count"
#     )
#     result = session.run(query, from_device_id=from_device_id, to_device_id=to_device_id).single()
#     return result["count"] > 0
#
# def most_recent_interaction(session: Session, device_id: str):
#     query = (
#         "MATCH (d:Device {device_id: $device_id})-[:CONNECTED]->(other:Device) "
#         "RETURN other ORDER BY r.timestamp DESC LIMIT 1"
#     )
#     return session.run(query, device_id=device_id).single()








# from flask import Blueprint, request, jsonify
# from app.db.database import driver
#
#
# def store_interaction(data):
#     # קבלת חיבור לבסיס הנתונים
#     with driver.session() as session:
#         interaction = data['interaction']
#         for device in devices:
#             query = (
#                 "MERGE (d:Device {id: $id}) "  # מיזוג צומת מכשיר לפי מזהה המכשיר (id)
#                 "SET d.brand = $brand, d.model = $model, d.os = $os, "  # הגדרת תכונות המכשיר (מותג, דגם, מערכת הפעלה)
#                 "d.latitude = $latitude, d.longitude = $longitude, "  # הגדרת מיקום המכשיר (קו רוחב, קו אורך)
#                 "d.altitude_meters = $altitude_meters, d.accuracy_meters = $accuracy_meters"  # הגדרת גובה ודיוק המיקום
#             )
#             session.run(query, **device['location'], **device)  # הרצת השאילתה עם הפרמטרים המתאימים
#
#         # יצירת קשר אינטראקציה בין המכשירים
#         query = (
#             "MATCH (from:Device {id: $from_device}), (to:Device {id: $to_device}) "  # התאמת המכשירים לפי מזהי המכשירים
#             "CREATE (from)-[r:CONNECTED {method: $method, bluetooth_version: $bluetooth_version, "  # יצירת קשר בין המכשירים עם פרטי האינטראקציה (שיטת חיבור, גרסת Bluetooth)
#             "signal_strength_dbm: $signal_strength_dbm, distance_meters: $distance_meters, "  # עוצמת האות ומרחק
#             "duration_seconds: $duration_seconds, timestamp: $timestamp}]->(to)"  # משך האינטראקציה וחותמת זמן
#         )
#         session.run(query, **interaction)  # הרצת השאילתה עם פרטי האינטראקציה
#
