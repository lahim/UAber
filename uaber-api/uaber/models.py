import uuid
import motor.motor_asyncio

from enum import Enum
from typing import Optional, List, Any

from pydantic import BaseModel
from pydantic.fields import PrivateAttr

from uaber import settings

db_client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.DATABASE['uri'], maxPoolSize=settings.DATABASE['max_pool_size']
)
db = db_client[settings.DATABASE['db_name']]


class Location(BaseModel):
    type: str = 'Point'
    coords: List[float]


class Address(BaseModel):
    zip_code: str
    city: str
    country: str


class VehicleType(str, Enum):
    MINI = 'MINI'
    SMALL = 'SMALL'
    MID = 'MID'
    SUV = 'SUV'
    BUS = 'BUS'


class Vehicle(BaseModel):
    vehicle_type: VehicleType
    number_of_places: int
    plate: str


class Driver(BaseModel):
    _id: str = PrivateAttr()
    uid: str
    name: str
    vehicle: Vehicle
    address: Address
    check_in_loc: Optional[Location] = None
    check_in_time: Optional[int] = None
    check_out_loc: Optional[Location] = None
    check_out_time: Optional[int] = None

    def __init__(self, **data: Any) -> None:
        data['uid'] = str(uuid.uuid4()) if not data.get('uid') else data['uid']
        super().__init__(**data)


class DriverCheckIn(BaseModel):
    pass


class BorderCrossingPoint(BaseModel):
    name: Optional[str] = None
    loc: Location


class DestinationPoint(BaseModel):
    name: str
    loc: Optional[Location] = None


class Refugee(BaseModel):
    name: str
    registration_number: str
    border_crossing_point: BorderCrossingPoint
    destination_point: DestinationPoint


class Trip(BaseModel):
    driver: Driver
    refugee: Refugee
    start_point: BorderCrossingPoint
    destination_point: DestinationPoint
