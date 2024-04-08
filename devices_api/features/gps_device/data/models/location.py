

from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import Mapped, relationship
from devices_api.core.models.postgres.models import Base
from devices_api.features.gps_device.domain.entities.gps_location_entity import GPSLocationEntity


class Location(Base):
    __tablename__ = "locations"

    longitude: Mapped[float] | float = Column(Float)
    latitude: Mapped[float] | float = Column(Float)
    device_id: Mapped[int] | int = Column(Integer)

    def to_entity(self) -> GPSLocationEntity:
        return GPSLocationEntity(
            id_=self.id,
            longitude=self.longitude,
            latitude=self.latitude,
            is_deleted=self.is_deleted,
            device_id=self.device_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
    
    @staticmethod
    def from_entity(entity: GPSLocationEntity) -> 'Location':
        return Location(
            id=entity.id_,
            longitude=entity.longitude,
            latitude=entity.latitude,
            is_deleted=entity.is_deleted,
            device=entity.device,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
