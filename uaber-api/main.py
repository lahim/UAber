from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from uaber import settings
from uaber.routers import driver, status

app = FastAPI()

app.include_router(status.router)
app.include_router(driver.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title="Code4Ukraine:UAber",
        version="0.0.1",
        description="API for UAber app",
        routes=app.routes,
    )
    schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
    }
    app.openapi_schema = schema
    return app.openapi_schema
