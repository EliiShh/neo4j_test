from dataclasses import dataclass
from .location import Location

@dataclass
class Device:
    id: str
    name: str
    brand: str
    model: str
    os: str
    location: Location
