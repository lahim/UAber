from fastapi import APIRouter

from uaber.models import Driver, Trip, Refugee, BorderCrossingPoint, DestinationPoint
from uaber.services import trip as trip_service

router = APIRouter(
    prefix='/trip',
    tags=['status'],
    responses={404: {'description': 'Not found'}}
)

@router.get('/')
async def get_drivers():
    return await trip_service.find_trips()


@router.put('/')
async def creat_trip(driver: Driver, refugee: Refugee, border: BorderCrossingPoint, destination: DestinationPoint) -> Trip:
    return await trip_service.create_trip(driver, refugee, border, destination)
