from abc import abstractmethod
from typing import Sequence, Tuple

from devices_api.core.use_cases.use_case import BaseUseCase
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel
from devices_api.features.gps_device.domain.services.gps_location_service import GPSLocationService



class GetGPSDeviceLocationsUseCase(BaseUseCase[None, Sequence[GPSLocationReadModel]]):
    """
    Use case class for getting all gps devices
    """

    service: GPSLocationService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[GPSLocationReadModel]:
        raise NotImplementedError()


class GetGPSDeviceLocationsUseCaseImpl(GetGPSDeviceLocationsUseCase):
    """
    Use case implementation for getting locations of gps device
    """

    def __init__(self, service: GPSLocationService):
        self.service: GPSLocationService = service

    def __call__(self, args: Tuple[str]) -> Sequence[GPSLocationReadModel]:
        try:
            device_id, = args
            gps_device_locations = self.service.find_all_by_device_id(device_id)
        except Exception as e:
            raise e

        return gps_device_locations
