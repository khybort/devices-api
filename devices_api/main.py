import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from devices_api.core.constant import WORKING_DIR, API_PREFIX
from devices_api.core.database.postgresql.database import engine
from devices_api.core.models.postgres import models
from devices_api.dependencies import settings
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import (
    gps_devices_router,
)

sys.path.append(WORKING_DIR)

app = FastAPI()
app.include_router(gps_devices_router, prefix=API_PREFIX)

origins = [
    settings.HOST_URL,
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This function is called when the app starts
    """
    models.Base.metadata.create_all(engine)  # pylint: disable=no-member
    yield


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
