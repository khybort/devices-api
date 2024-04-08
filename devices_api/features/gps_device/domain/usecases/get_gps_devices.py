from abc import abstractmethod
from typing import Sequence

from devices_api.core.use_cases.use_case import BaseUseCase
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.services.gps_device_service import GPSDeviceService



class GetGPSDevicesUseCase(BaseUseCase[None, Sequence[GPSDeviceReadModel]]):
    """
    Use case class for getting all gps devices
    """

    service: GPSDeviceService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[GPSDeviceReadModel]:
        raise NotImplementedError()


class GetGPSDevicesUseCaseImpl(GetGPSDevicesUseCase):
    """
    Use case implementation for getting all gps devices
    """

    def __init__(self, service: GPSDeviceService):
        self.service: GPSDeviceService = service

    def __call__(self, args: None) -> Sequence[GPSDeviceReadModel]:
        try:
            gps_devices = self.service.find_all()
        except Exception as e:
            raise e

        return gps_devices
