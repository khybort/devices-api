from sqlalchemy.orm import Session

from devices_api.features.gps_device.domain.repositories.gps_device_repository import GPSDeviceRepository
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import GPSDeviceUnitOfWork


class GPSDeviceUnitOfWorkImpl(GPSDeviceUnitOfWork):
    """
    GPSDeviceUnitOfWorkImpl implements Unit of Work pattern for GPS device
    """

    def __init__(self, session: Session, gps_device_repository: GPSDeviceRepository):
        self.session: Session = session
        self.repository: GPSDeviceRepository = gps_device_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()