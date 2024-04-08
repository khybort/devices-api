"""
This module contains all services for GPS devices
"""

from abc import abstractmethod
from devices_api.core.services.base_service import BaseService
from devices_api.features.gps_device.domain.entities.gps_device_create_model import GPSDeviceCreateModel
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import GPSDeviceUnitOfWork


class GPSDeviceService(BaseService):
    """
    Interface for GPSDeviceService
    """
    unit_of_work: GPSDeviceUnitOfWork
    @abstractmethod
    def find_by_name(self, name: str):
        raise NotImplementedError()
    @abstractmethod
    def create(self, data: GPSDeviceCreateModel):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, device_id: int):
        raise NotImplementedError()

