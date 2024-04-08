from abc import abstractmethod
from typing import Tuple

from devices_api.core.use_cases.use_case import BaseUseCase
from devices_api.features.gps_device.domain.entities.gps_device_create_model import GPSDeviceCreateModel
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.services.gps_device_service import GPSDeviceService



class CreateGPSDeviceUseCase(BaseUseCase[Tuple[GPSDeviceCreateModel], GPSDeviceReadModel]):
    gps_device_service: GPSDeviceService

    @abstractmethod
    def __call__(self, args: Tuple[GPSDeviceCreateModel]) -> GPSDeviceReadModel:
        raise NotImplementedError()


class CreateGPSDeviceUseCaseImpl(CreateGPSDeviceUseCase):

    def __init__(self, gps_device_service: GPSDeviceService):
        self.gps_device_service: GPSDeviceService = gps_device_service

    def __call__(self, args: Tuple[GPSDeviceCreateModel]) -> GPSDeviceReadModel:
        data, = args
        gps_device: GPSDeviceReadModel = self.gps_device_service.create(data)
        return gps_device
