


from datetime import datetime
from pydantic import BaseModel, Field

from devices_api.features.gps_device.domain.entities.gps_location_entity import GPSLocationEntity


class GPSLocationReadModel(BaseModel):
    id: int = Field(example=1)
    latitude: float = Field(example=-79.132557)
    longitude: float = Field(example=35.132557)
    device_id: int = Field(example=1)
    is_deleted: bool = Field(example=True)
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(entity: GPSLocationEntity) -> 'GPSLocationReadModel':
        """
        return GPSLocationReadModel from GPSLocationEntity
        """
        return GPSLocationReadModel(
            id=entity.id_,
            latitude=entity.latitude,
            longitude=entity.longitude,
            device_id=entity.device_id,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
    