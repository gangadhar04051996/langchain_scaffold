from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class TemperatureResponseModel():
    location: str
    temperature: str