from abc import abstractmethod
from typing import Sequence

from devices_api.core.repositories.base_repository import BaseRepository
from devices_api.features.gps_device.domain.entities.gps_location_entity import GPSLocationEntity


class GPSLocationRepository(BaseRepository[GPSLocationEntity]):
    """GPSLocationRepository defines a repositories interface for GPSLocation entity"""
    
    @abstractmethod
    def find_all_by_device_id(self, device_id: int) -> Sequence[GPSLocationEntity]:
        raise NotImplementedError()
    
    @abstractmethod
    def find_last_location(self, device_id: int) -> GPSLocationEntity:
        raise NotImplementedError()