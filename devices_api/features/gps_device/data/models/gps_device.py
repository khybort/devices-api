
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, mapped_column

from devices_api.core.models.postgres.models import Base
from devices_api.features.gps_device.domain.entities.gps_device_entity import GPSDeviceEntity

class GPSDevice(Base):
    """
    GPSDevice DTO is an object associated with gps_device entity
    """
    __tablename__ = "gps_devices"
    
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

    def to_dict(self):
        """
        return dict representation of object
        """
        return {
            "id": self.id,
            "name": self.name,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def to_entity(self) -> GPSDeviceEntity:
        """
        return entity representation of object
        """
        return GPSDeviceEntity(
            id_= self.id,
            name=self.name,
            is_deleted=self.is_deleted,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
    
    @staticmethod
    def from_entity(entity: GPSDeviceEntity) -> 'GPSDevice':
        """
        return GPSDevice from GPSDeviceEntity
        """
        return GPSDevice(
            id=entity.id_,
            name=entity.name,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
