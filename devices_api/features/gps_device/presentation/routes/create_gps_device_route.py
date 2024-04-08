from fastapi import Depends, HTTPException, status, Response, Request

from devices_api.core.exception.gps_device_exception import GPSDeviceAlreadyExistsError
from devices_api.features.gps_device.dependencies import get_create_gps_device_use_case
from devices_api.features.gps_device.domain.entities.gps_device_create_model import GPSDeviceCreateModel
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.usecases.create_gps_device import CreateGPSDeviceUseCase
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import router
from devices_api.features.gps_device.presentation.schemas.gps_device_error_message import ErrorMessageGPSDeviceAlreadyExists
from devices_api.core.logger import logger


@router.post(
    '/',
    response_model=GPSDeviceReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageGPSDeviceAlreadyExists
        }
    },
)
def create_gps_device(
    data: GPSDeviceCreateModel,
    response: Response,
    request: Request,
    create_gps_device_use_case: CreateGPSDeviceUseCase = Depends(get_create_gps_device_use_case),
):
    try:
        gps_device = create_gps_device_use_case((data, ))
    except GPSDeviceAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        ) from exception
    except Exception as _exception:
        logger.error(_exception)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from _exception

    response.headers['location'] = f"{request.url.path}{gps_device.id}"
    return gps_device
