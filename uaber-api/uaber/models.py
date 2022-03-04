import uuid
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel
from pydantic.fields import PrivateAttr


class Location(BaseModel):
    type: str = "Point"
    coords: List[float]


class Address(BaseModel):
    zip_code: str
    city: str
    country: str


class VehicleType(str, Enum):
    MINI = "MINI"
    SMALL = "SMALL"
    MID = "MID"
    SUV = "SUV"
    BUS = "BUS"


class Vehicle(BaseModel):
    vehicle_type: VehicleType
    number_of_places: int
    plate: str


class DriverActionType(str, Enum):
    CHECK_IN = "CHECK_IN"
    CHECK_OUT = "CHECK_OUT"
    ABORT = "ABORT"


class DriverAction(BaseModel):
    loc: Location
    action_type: DriverActionType
    time: int


class DriverCheckIn(DriverAction):
    action_type: DriverActionType = DriverActionType.CHECK_IN


class DriverCheckOut(DriverAction):
    action_type: DriverActionType = DriverActionType.CHECK_OUT


class Driver(BaseModel):
    _id: str = PrivateAttr()
    uid: str
    name: str
    vehicle: Vehicle
    address: Address
    check_in: Optional[DriverCheckIn] = None
    check_out: Optional[DriverCheckOut] = None

    def __init__(self, **data: Any) -> None:
        data["uid"] = str(uuid.uuid4()) if not data.get("uid") else data["uid"]
        super().__init__(**data)


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
