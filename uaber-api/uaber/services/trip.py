from typing import List

from . import db
from ..models import Trip, Driver, Refugee, BorderCrossingPoint, DestinationPoint


async def find_trips() -> List[Trip]:
    results = []
    async for doc in db.trips.find({}):  # todo: add some filtering
        results.append(Trip(**doc))
    return results


async def create_trip(driver: Driver, refugee: Refugee, border: BorderCrossingPoint, destination: DestinationPoint) -> Trip:
    trip = Trip(driver=driver, refugee=refugee, start_point=border, destination_point=destination)
    await db.trips.insert_one(trip.dict())
    return trip
