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
    number: str
    entry: bool
    car_type: CarType
    photo: Union[str, None] = None

class PassInfoUpdate(BaseModel):
    datetime: Union[datetime, None] = None #??
    number: Union[str, None] = None
    entry: Union[bool, None] = None
    car_type: Union[CarType, None] = None
    photo: Union[str, None] = None