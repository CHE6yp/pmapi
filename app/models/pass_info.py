from pydantic import BaseModel
from typing import Union
from enum import Enum
from datetime import datetime

class CarType(str, Enum):
    other = "other"
    police = "police"
    ambulance = "ambulance"
    fire = "fire"

class PassInfo(BaseModel):
    datetime: datetime
    number: int
    entry: bool
    car_type: CarType
    photo: Union[str, None] = None