from devices_api.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from devices_api.features.gps_device.domain.repositories.gps_location_repository import GPSLocationRepository


class GPSLocationUnitOfWork(AbstractUnitOfWork[GPSLocationRepository]):
    """
    defines an interface based on Unit of Work
    """
    pass