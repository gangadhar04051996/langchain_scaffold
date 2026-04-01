from pydantic import BaseModel
from dataclasses import dataclass

# @dataclass
class TemperatureResponseModel(BaseModel):
    location: str
    temperature: str