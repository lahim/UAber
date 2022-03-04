from fastapi import APIRouter

from uaber.models import Driver, Trip, Refugee, BorderCrossingPoint, DestinationPoint
from uaber.services import driver as driver_service

router = APIRouter(
    prefix='/drivers',
    tags=['status'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
async def get_drivers():
    return await driver_service.find_drivers()


@router.post('/')
async def create_driver(driver: Driver) -> Driver:
    return await driver_service.create_driver(driver)


@router.put('/{id}/checkin')
async def update_diver_check_in(driver_id: str) -> Driver:
    return await driver_service.update_diver.check_in_driver(driver_id)


@router.put('/{id}/checkout')
async def update_diver_check_in(driver_id: str) -> Driver:
    return await driver_service.update_diver.check_out_driver(driver_id)
