from fastapi import Depends, HTTPException, status

from devices_api.features.gps_device.dependencies import get_gps_device_locations_use_case
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel
from devices_api.features.gps_device.domain.usecases.get_gps_device_locations import GetGPSDeviceLocationsUseCase
from devices_api.features.gps_device.presentation.schemas.gps_device_error_message import ErrorMessageGPSDevicesNotFound
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import router
from devices_api.core.logger import logger

@router.get(
    '/{device_id}',
    response_model=list[GPSLocationReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageGPSDevicesNotFound
        }
    }
)
def get_gps_device_locations(device_id: int, skip: int = 0, limit: int = 10, get_gps_device_locations_use_case_: GetGPSDeviceLocationsUseCase = Depends(get_gps_device_locations_use_case)) -> list[GPSLocationReadModel]:
    try:
        gps_device_locations = get_gps_device_locations_use_case_((device_id,))
    except Exception as exc:
        logger.error(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from exc

    return gps_device_locations
