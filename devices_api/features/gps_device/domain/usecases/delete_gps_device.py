from abc import abstractmethod
from typing import Tuple

from devices_api.core.use_cases.use_case import BaseUseCase
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import GPSDeviceUnitOfWork
from devices_api.features.gps_device.domain.services.gps_device_service import GPSDeviceService


class DeleteGPSDeviceUseCase(BaseUseCase[Tuple[int], GPSDeviceReadModel]):
    """
    Delete GPS device use case
    """
    @abstractmethod
    def __call__(self, args: Tuple[int]) -> GPSDeviceReadModel:
        raise NotImplementedError()


class DeleteGPSDeviceUseCaseImpl(DeleteGPSDeviceUseCase):
    def __init__(self, gps_device_service: GPSDeviceService):
        self.gps_device_service: GPSDeviceService = gps_device_service

    def __call__(self, args: Tuple[int]) -> GPSDeviceReadModel:
        device_id, = args
        gps_device = self.gps_device_service.delete(device_id)
        return gps_device

