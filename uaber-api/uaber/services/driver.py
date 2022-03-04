from typing import List

from . import db
from ..models import Driver


async def find_drivers() -> List[Driver]:
    results = []
    async for doc in db.drivers.find({}):  # todo: add some filtering
        results.append(Driver(**doc))
    return results


async def create_driver(driver: Driver) -> Driver:
    await db.drivers.insert_one(driver.dict())
    return driver
