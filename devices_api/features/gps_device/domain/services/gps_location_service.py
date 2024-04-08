from abc import abstractmethod
from typing import Sequence
from devices_api.core.services.base_service import BaseService
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel

class GPSLocationService(BaseService):
    """
    Interface for LocationService
    """
    @abstractmethod
    def find_all_by_device_id(self, device_id: str) -> Sequence[GPSLocationReadModel]:
        raise NotImplementedError()
    @abstractmethod
    def find_last_locations(self) -> Sequence[GPSLocationReadModel]:
        raise NotImplementedError()

