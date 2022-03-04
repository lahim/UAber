from fastapi import APIRouter

router = APIRouter(
    prefix="/status", tags=["status"], responses={404: {"description": "Not found"}}
)


@router.get("/")
async def healthcheck():
    # todo: add some checks here!
    return {"message": "ok"}
