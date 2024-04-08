from pydantic import BaseModel, Field

from devices_api.core.exception.gps_device_exception import (
    GPSDeviceNotFoundError,
    GPSDevicesNotFoundError,
    GPSDeviceAlreadyExistsError
)


class ErrorMessageGPSDeviceNotFound(BaseModel):
    detail: str = Field(example=GPSDeviceNotFoundError.message)


class ErrorMessageGPSDevicesNotFound(BaseModel):
    detail: str = Field(example=GPSDevicesNotFoundError.message)


class ErrorMessageGPSDeviceAlreadyExists(BaseModel):
    detail: str = Field(example=GPSDeviceAlreadyExistsError.message)