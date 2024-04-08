from typing import Sequence
from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from devices_api.features.gps_device.domain.entities.gps_device_entity import GPSDeviceEntity
from devices_api.features.gps_device.domain.repositories.gps_device_repository import GPSDeviceRepository
from devices_api.features.gps_device.data.models.gps_device import GPSDevice


class GPSDeviceRepositoryImpl(GPSDeviceRepository):
    """
        GPSDeviceRepositoryImpl implements CRUD operations related GPS device entity using SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session: Session = session

    def find_all(self) -> Sequence[GPSDeviceEntity]:
        # TODO: add offset and limit
        try:
            statement = select(GPSDevice).filter_by(is_deleted=False)
            results: Sequence[GPSDevice] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []
        except Exception as e:
            raise e
        return [result.to_entity() for result in results]

    def find_by_name(self, name: str) -> GPSDeviceEntity | None:
        statement = select(GPSDevice).filter_by(name=name, is_deleted=False)
        try:
            result = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
        return result.to_entity()

    def find_by_device_id(self, device_id: int) -> GPSDeviceEntity | None:
        statement = select(GPSDevice).filter_by(id=device_id, is_deleted=False)
        try:
            result = self.session.execute(statement).scalar_one()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
        return result.to_entity()
    
    def create(self, entity: GPSDeviceEntity) -> GPSDeviceEntity:
        gps_device = GPSDevice.from_entity(entity)
        self.session.add(gps_device)
        return gps_device.to_entity()
    
    def update(self, entity: GPSDeviceEntity) -> GPSDeviceEntity:
        gps_device = GPSDevice.from_entity(entity)
        update_data = gps_device.to_dict()

        for key in [GPSDevice.updated_at.key, GPSDevice.created_at.key, GPSDevice.id.key]:
            update_data.pop(key)

        statement = update(GPSDevice).where(GPSDevice.id == entity.id_).values(**update_data).returning(GPSDevice)
        gps_device_mapping = self.session.execute(statement).mappings().one()
        print(gps_device_mapping)
        return gps_device_mapping["GPSDevice"].to_entity()
