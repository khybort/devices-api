from datetime import datetime

class GPSLocationEntity(object):
    """
        GPSLocation represents collection of locations as an entity
    """
    def __init__(
            self,
            id_: int | None,
            longitude: str,
            latitude: str,
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            is_deleted: bool = False,
            device_id: int= None):
        self.id_ = id_
        self.longitude = longitude
        self.latitude = latitude
        self.is_deleted = is_deleted
        self.device_id = device_id if device_id is not None else None
        self.created_at = created_at
        self.updated_at = updated_at
    
    def to_popo(self) -> object:
        return self.__dict__
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, GPSLocationEntity):
            return self.id_ == other.id_
        return False
    
    
