from typing import List

from . import db
from ..models import Driver, DriverCheckIn, DriverCheckOut


async def find_drivers() -> List[Driver]:
    results = []
    async for doc in db.drivers.find({}):  # todo: add some filtering
        results.append(Driver(**doc))
    return results


async def create_driver(driver: Driver) -> Driver:
    await db.drivers.insert_one(driver.dict())
    return driver


async def check_in_driver(driver_id: str):
    driver_check_in = DriverCheckIn() # todo: add localization
    update_result = await db.drivers.update_one({"_id": driver_id}, {"check_in": driver_check_in})
    return check_updated_driver(update_result, driver_id)


async def check_out_driver(driver_id: str):
    driver_check_out = DriverCheckOut() # todo: add localization
    update_result = await db.drivers.update_one({"_id": driver_id}, {"check_in": driver_check_out})
    return check_updated_driver(update_result, driver_id)


async def check_updated_driver(result, driver_id) -> Driver:
    if result.modified_count == 1:
        if (updated_driver := await db.driver.find_one({"_id": driver_id})) is not None:
            return updated_driver
    if (existing_driver := await db["students"].find_one({"_id": driver_id})) is not None:
        return existing_driver
