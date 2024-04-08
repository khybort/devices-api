from typing import Sequence
from devices_api.features.gps_device.domain.entities.gps_location_read_model import GPSLocationReadModel
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import GPSDeviceUnitOfWork
from devices_api.features.gps_device.domain.repositories.gps_location_unit_of_work import GPSLocationUnitOfWork
from devices_api.features.gps_device.domain.services.gps_location_service import GPSLocationService


class GPSLocationServiceImpl(GPSLocationService):
    """
    Implementation of GPSDeviceService
    """

    def __init__(self, unit_of_work: GPSLocationUnitOfWork,
                 gps_device_unit_of_work: GPSDeviceUnitOfWork):
        self.unit_of_work: GPSLocationUnitOfWork = unit_of_work
        self.gps_device_unit_of_work: GPSDeviceUnitOfWork = gps_device_unit_of_work
    
    def find_all(self) -> Sequence[GPSLocationReadModel]:
        all_gps_locations = self.unit_of_work.repository.find_all()
        return [GPSLocationReadModel.from_entity(gps_location) for gps_location in all_gps_locations]

    def find_all_by_device_id(self, device_id: str) -> Sequence[GPSLocationReadModel]:
        gps_device_locations = self.unit_of_work.repository.find_all_by_device_id(device_id)
        return [GPSLocationReadModel.from_entity(gps_device_location) for gps_device_location in gps_device_locations]
    
    def find_last_locations(self) -> Sequence[GPSLocationReadModel]:
        last_locations = []
        gps_devices = self.gps_device_unit_of_work.repository.find_all()
        for gps_device in gps_devices:
            last_location = self.unit_of_work.repository.find_last_location(gps_device.id_)
            if not last_locations:
                last_locations.append(GPSLocationReadModel.from_entity(last_location))
        return last_locations
