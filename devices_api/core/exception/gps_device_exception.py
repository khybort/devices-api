"""
    GPS Device exceptions
"""
from devices_api.core.exception.base_exception import BaseException


class GPSDeviceNotFoundError(BaseException):
    message = 'GPS Device does not exist.'


class GPSDevicesNotFoundError(BaseException):
    message = 'GPS Devices do not exist'


class GPSDeviceAlreadyExistsError(BaseException):
    message = 'GPS Device already exists'

