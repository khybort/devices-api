from abc import abstractmethod
from typing import Sequence

from devices_api.core.repositories.base_repository import BaseRepository
from devices_api.features.gps_device.domain.entities.gps_device_entity import GPSDeviceEntity


class GPSDeviceRepository(BaseRepository[GPSDeviceEntity]):
    """GPSDeviceRepository defines a repositories interface for GPSDevice entity"""

    @abstractmethod
    def find_all(self) -> Sequence[GPSDeviceEntity]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(self, name: str) -> GPSDeviceEntity | None:
        raise NotImplementedError()
    
    @abstractmethod
    def find_by_device_id(self, device_id: int) -> GPSDeviceEntity | None:
        raise NotImplementedError()
    
    @abstractmethod
    def create(self, entity: GPSDeviceEntity) -> GPSDeviceEntity:
        raise NotImplementedError()
    @abstractmethod
    def update(self, entity: GPSDeviceEntity) -> GPSDeviceEntity:
        raise NotImplementedError()
