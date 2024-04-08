from sqlalchemy.orm import Session

from devices_api.features.gps_device.domain.repositories.gps_location_repository import GPSLocationRepository
from devices_api.features.gps_device.domain.repositories.gps_location_unit_of_work import GPSLocationUnitOfWork


class GPSLocationUnitOfWorkImpl(GPSLocationUnitOfWork):
    """
    GPSLocationUnitOfWorkImpl implements Unit of Work pattern for GPS location
    """

    def __init__(self, session: Session, gps_location_repository: GPSLocationRepository):
        self.session: Session = session
        self.repository: GPSLocationRepository = gps_location_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()