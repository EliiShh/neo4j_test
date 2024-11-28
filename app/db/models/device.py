from dataclasses import dataclass
from app.db.models import Location

@dataclass
class Device:
    device_id: str
    name: str
    brand: str
    model: str
    os: str
    location: Location
