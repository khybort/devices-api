import copy
from datetime import datetime

from devices_api.core.exception.invalid_operation_exception import InvalidOperationError


class GPSDeviceEntity(object):
    """
    GPSDevice represents collection of devices as an entity
    """
    def __init__(
            self,
            id_: int | None,
            name: str,
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            is_deleted: bool = False):
        self.id_ = id_
        self.name = name
        self.is_deleted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, GPSDeviceEntity):
            return self.id_ == other.id_
        return False

    def to_popo(self) -> object:
        return self.__dict__
    
    def marked_entity_as_deleted(self) -> 'GPSDeviceEntity':
        if self.is_deleted:
            raise InvalidOperationError("GPSDevice already marked as deleted")
        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True
        return marked_entity
