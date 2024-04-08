from abc import abstractmethod
from typing import Sequence, Tuple

from devices_api.core.use_cases.use_case import BaseUseCase
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel
from devices_api.features.gps_device.domain.services.gps_location_service import GPSLocationService


class GetGPSLastLocationsUseCase(BaseUseCase[None, Sequence[GPSLocationReadModel]]):
    """
    use case for get last locations of gps devices
    """
    
    service: GPSLocationService
    @abstractmethod
    def __call__(self, args: None) -> Sequence[GPSLocationReadModel]:
        raise NotImplementedError()

class GetGPSLastLocationsUseCaseImpl(GetGPSLastLocationsUseCase):
    """
    Use case implementation for getting last locations of gps devices
    """
    def __init__(self, service: GPSLocationService):
        self.service: GPSLocationService = service

    def __call__(self, args: None) -> Sequence[GPSLocationReadModel]:
        try:
            gps_device_locations = self.service.find_last_locations()
        except Exception as e:
            raise e

        return gps_device_locations
