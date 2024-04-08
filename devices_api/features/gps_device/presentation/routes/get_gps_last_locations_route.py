from fastapi import Depends, HTTPException, status

from devices_api.features.gps_device.dependencies import get_gps_device_locations_use_case, get_gps_last_locations_use_case
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel
from devices_api.features.gps_device.domain.usecases.get_gps_device_locations import GetGPSDeviceLocationsUseCase
from devices_api.features.gps_device.domain.usecases.get_gps_last_locations import GetGPSLastLocationsUseCase
from devices_api.features.gps_device.presentation.schemas.gps_device_error_message import ErrorMessageGPSDevicesNotFound
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import router
from devices_api.core.logger import logger

@router.get(
    '/last-locations',
    response_model=list[GPSLocationReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageGPSDevicesNotFound
        }
    }
)
def get_gps_last_locations(skip: int = 0, limit: int = 10, get_gps_last_locations_use_case_: GetGPSLastLocationsUseCase = Depends(get_gps_last_locations_use_case)) -> list[GPSLocationReadModel]:
    try:
        gps_last_locations = get_gps_last_locations_use_case_(None)
    except Exception as exc:
        logger.error(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from exc

    return gps_last_locations
