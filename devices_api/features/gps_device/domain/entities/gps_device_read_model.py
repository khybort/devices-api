from pydantic import BaseModel, Field
from datetime import datetime

from devices_api.features.gps_device.domain.entities.gps_device_entity import GPSDeviceEntity


class GPSDeviceReadModel(BaseModel):
    """
    GPSDeviceReadModel represents collection of devices as a read model
    """

    id: int = Field(example=1)
    name: str = Field(example="GPS Device 1")
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: GPSDeviceEntity) -> 'GPSDeviceReadModel':
        """
        return GPSDeviceReadModel from GPSDeviceEntity
        """
        return GPSDeviceReadModel(
            id=entity.id_,
            name=entity.name,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
