import motor.motor_asyncio

from uaber import settings

db_client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.DATABASE["uri"], maxPoolSize=settings.DATABASE["max_pool_size"]
)
db = db_client[settings.DATABASE["db_name"]]

__all__ = ["db"]
