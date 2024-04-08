from typing import Sequence
from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from devices_api.features.gps_device.domain.entities.gps_location_entity import GPSLocationEntity
from devices_api.features.gps_device.data.models.location import Location
from devices_api.features.gps_device.domain.repositories.gps_location_repository import GPSLocationRepository


class GPSLocationRepositoryImpl(GPSLocationRepository):
    """
        GPSLocationRepositoryImpl implements CRUD operations related GPS device location entity using SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session: Session = session
 
    def find_all(self) -> Sequence[GPSLocationEntity]:
        statement = select(Location).filter_by(is_deleted=False)
        try:
            results = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []
        except Exception as e:
            raise e
        return [result.to_entity() for result in results]
    
    def find_all_by_device_id(self, device_id: str) -> Sequence[GPSLocationEntity]:
        statement = select(Location).filter_by(device_id=device_id, is_deleted=False)
        try:
            results = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []
        except Exception as e:
            raise e
        return [result.to_entity() for result in results]

    def find_last_location(self, device_id: int) -> GPSLocationEntity | None:

        statement = select(Location).filter_by(device_id=device_id, is_deleted=False).order_by(Location.created_at.desc()).limit(1)
        try:
            result = self.session.execute(statement).scalar_one_or_none()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
        return result.to_entity() if result else None
