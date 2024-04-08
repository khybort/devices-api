from fastapi import Depends, HTTPException, status

from devices_api.features.gps_device.dependencies import get_gps_devices_use_case
from devices_api.features.gps_device.presentation.schemas.gps_device_error_message import ErrorMessageGPSDevicesNotFound
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.usecases.get_gps_devices import GetGPSDevicesUseCase
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import router
from devices_api.core.logger import logger

@router.get(
    '/',
    response_model=list[GPSDeviceReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageGPSDevicesNotFound
        }
    }
)
def get_gps_devices(skip: int = 0, limit: int = 100, get_gps_devices_use_case_: GetGPSDevicesUseCase = Depends(get_gps_devices_use_case)) -> list[GPSDeviceReadModel]:
    try:
        gps_devices = get_gps_devices_use_case_(None)
    except Exception as exc:
        logger.error(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from exc

    return gps_devices
