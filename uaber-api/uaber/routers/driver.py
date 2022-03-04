from fastapi import APIRouter

from uaber.models import Driver
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


# todo: add rest api endpoints below
