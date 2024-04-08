"""
Delete GPS device route
"""
from fastapi import APIRouter, Depends, HTTPException, status

from devices_api.core.exception.gps_device_exception import GPSDeviceNotFoundError
from devices_api.features.gps_device.dependencies import get_delete_gps_device_use_case
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.usecases.delete_gps_device import DeleteGPSDeviceUseCase
from devices_api.features.gps_device.presentation.schemas.gps_device_error_message import ErrorMessageGPSDevicesNotFound
from devices_api.features.gps_device.presentation.routes.gps_devices_routes import router
from devices_api.core.logger import logger

@router.delete(
    '/{device_id}',
    response_model=GPSDeviceReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageGPSDevicesNotFound
        }
    }
)
def delete_gps_device(device_id: int, delete_gps_device_use_case_: DeleteGPSDeviceUseCase = Depends(get_delete_gps_device_use_case)) -> GPSDeviceReadModel:
    try:
        gps_device = delete_gps_device_use_case_((device_id,))
    except GPSDeviceNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.message
        ) from exc
    except Exception as exc:
        logger.error(exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) from exc

    return gps_device
