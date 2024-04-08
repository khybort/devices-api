

from typing import Sequence, cast
from devices_api.core.exception.gps_device_exception import GPSDeviceAlreadyExistsError, GPSDeviceNotFoundError
from devices_api.features.gps_device.domain.entities.gps_device_create_model import GPSDeviceCreateModel
from devices_api.features.gps_device.domain.entities.gps_device_entity import GPSDeviceEntity
from devices_api.features.gps_device.domain.entities.gps_device_read_model import GPSDeviceReadModel
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import GPSDeviceUnitOfWork
from devices_api.features.gps_device.domain.services.gps_device_service import GPSDeviceService


class GPSDeviceServiceImpl(GPSDeviceService):
    """
    Implementation of GPSDeviceService
    """
    def __init__(self, unit_of_work: GPSDeviceUnitOfWork):
        self.unit_of_work: GPSDeviceUnitOfWork = unit_of_work

    def find_all(self) -> Sequence[GPSDeviceReadModel]:
        devices = self.unit_of_work.repository.find_all()
        return [GPSDeviceReadModel.from_entity(device) for device in devices]
    
    def find_by_name(self, name: str) -> GPSDeviceReadModel | None:
        device = self.unit_of_work.repository.find_by_name(name)
        if device is None:
            return None
        return GPSDeviceReadModel.from_entity(device)
    
    def create(self, data: GPSDeviceCreateModel) -> GPSDeviceReadModel:
        gps_device = GPSDeviceEntity(
            id_=None,
            **data.dict()
        )
        existing_gps_device = self.find_by_name(gps_device.name)
        if existing_gps_device is not None:
            raise GPSDeviceAlreadyExistsError()

        try:
            self.unit_of_work.repository.create(gps_device)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        created_gps_device = self.unit_of_work.repository.find_by_name(data.name)

        return GPSDeviceReadModel.from_entity(cast(GPSDeviceEntity, created_gps_device))
    
    def delete(self, device_id: int) -> None:
        existing_gps_device = self.unit_of_work.repository.find_by_device_id(device_id)
        if existing_gps_device is None:
            raise GPSDeviceNotFoundError()
        marked_gps_device = existing_gps_device.marked_entity_as_deleted()
        try:
            deleted_gps_device = self.unit_of_work.repository.update(marked_gps_device)
            self.unit_of_work.commit()
        except Exception as _e:
            self.unit_of_work.rollback()
            raise
        return GPSDeviceReadModel.from_entity(cast(GPSDeviceEntity, deleted_gps_device))
