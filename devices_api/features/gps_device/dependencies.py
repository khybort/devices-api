"""
This module contains all dependencies for GPS devices
"""

from fastapi import Depends
from sqlalchemy.orm import Session


from devices_api.features.gps_device.data.repositories.gps_device_repository_impl import (
    GPSDeviceRepositoryImpl,
)
from devices_api.features.gps_device.data.repositories.gps_device_unit_of_work_impl import (
    GPSDeviceUnitOfWorkImpl,
)
from devices_api.features.gps_device.data.repositories.gps_location_repository_impl import (
    GPSLocationRepositoryImpl,
)
from devices_api.features.gps_device.data.repositories.gps_location_unit_of_work_impl import (
    GPSLocationUnitOfWorkImpl,
)
from devices_api.features.gps_device.data.services.gps_device_service_impl import (
    GPSDeviceServiceImpl,
)
from devices_api.features.gps_device.data.services.gps_location_service_impl import (
    GPSLocationServiceImpl,
)
from devices_api.features.gps_device.domain.repositories.gps_device_repository import (
    GPSDeviceRepository,
)
from devices_api.features.gps_device.domain.repositories.gps_device_unit_of_work import (
    GPSDeviceUnitOfWork,
)
from devices_api.features.gps_device.domain.repositories.gps_location_repository import (
    GPSLocationRepository,
)
from devices_api.features.gps_device.domain.repositories.gps_location_unit_of_work import (
    GPSLocationUnitOfWork,
)
from devices_api.features.gps_device.domain.services.gps_device_service import (
    GPSDeviceService,
)
from devices_api.core.database.postgresql.database import get_session
from devices_api.features.gps_device.domain.services.gps_location_service import (
    GPSLocationService,
)
from devices_api.features.gps_device.domain.usecases.create_gps_device import (
    CreateGPSDeviceUseCase,
    CreateGPSDeviceUseCaseImpl,
)
from devices_api.features.gps_device.domain.usecases.delete_gps_device import DeleteGPSDeviceUseCase, DeleteGPSDeviceUseCaseImpl
from devices_api.features.gps_device.domain.usecases.get_gps_device_locations import (
    GetGPSDeviceLocationsUseCase,
    GetGPSDeviceLocationsUseCaseImpl,
)
from devices_api.features.gps_device.domain.usecases.get_gps_devices import (
    GetGPSDevicesUseCaseImpl,
    GetGPSDevicesUseCase,
)
from devices_api.features.gps_device.domain.usecases.get_gps_last_locations import GetGPSLastLocationsUseCase, GetGPSLastLocationsUseCaseImpl


def get_gps_device_repository(
    session: Session = Depends(get_session),
) -> GPSDeviceRepository:
    """
    GPSDeviceRepositoryImpl implements CRUD operations related GPS device entity using SQLAlchemy
    """
    return GPSDeviceRepositoryImpl(session)


def get_gps_location_repository(
    session: Session = Depends(get_session),
) -> GPSLocationRepository:
    """
    GPSLocationRepositoryImpl implements CRUD operations related GPS location entity using SQLAlchemy
    """
    return GPSLocationRepositoryImpl(session)


def get_gps_device_unit_of_work(
    session: Session = Depends(get_session),
    gps_device_repository: GPSDeviceRepository = Depends(get_gps_device_repository),
) -> GPSDeviceUnitOfWork:
    """
    GPSDeviceUnitOfWorkImpl implements Unit of Work pattern for GPS device
    """
    return GPSDeviceUnitOfWorkImpl(session, gps_device_repository)


def get_gps_location_unit_of_work(
    session: Session = Depends(get_session),
    gps_location_repository: GPSLocationRepository = Depends(
        get_gps_location_repository
    ),
) -> GPSLocationUnitOfWork:
    """
    GPSLocationUnitOfWorkImpl implements Unit of Work pattern for GPS location
    """
    return GPSLocationUnitOfWorkImpl(session, gps_location_repository)


def get_gps_device_service(
    gps_device_unit_of_work: GPSDeviceUnitOfWork = Depends(get_gps_device_unit_of_work),
) -> GPSDeviceService:
    """
    Service factory for gps devices
    """
    return GPSDeviceServiceImpl(gps_device_unit_of_work)


def get_gps_location_service(
    gps_location_unit_of_work: GPSLocationUnitOfWork = Depends(
        get_gps_location_unit_of_work), 
    gps_device_unit_of_work: GPSDeviceUnitOfWork = Depends(
        get_gps_device_unit_of_work
    ),
) -> GPSLocationService:
    """
    Service factory for gps locations
    """
    return GPSLocationServiceImpl(gps_location_unit_of_work, gps_device_unit_of_work)


def get_gps_devices_use_case(
    gps_device_service: GPSDeviceService = Depends(get_gps_device_service),
) -> GetGPSDevicesUseCase:
    """
    Use case factory for getting all gps devices
    """
    return GetGPSDevicesUseCaseImpl(gps_device_service)


def get_create_gps_device_use_case(
    gps_device_service: GPSDeviceService = Depends(get_gps_device_service),
) -> CreateGPSDeviceUseCase:
    """
    Use case factory for creating gps device
    """
    return CreateGPSDeviceUseCaseImpl(gps_device_service)


def get_gps_device_locations_use_case(
    gps_location_service: GPSLocationService = Depends(get_gps_location_service),
) -> GetGPSDeviceLocationsUseCase:
    """
    Use case factory for getting gps device locations
    """
    return GetGPSDeviceLocationsUseCaseImpl(gps_location_service)

def get_delete_gps_device_use_case(
    gps_device_service: GPSDeviceService = Depends(get_gps_device_service),
) -> DeleteGPSDeviceUseCase:
    """
    Use case factory for deleting gps device
    """
    return DeleteGPSDeviceUseCaseImpl(gps_device_service)

def get_gps_last_locations_use_case(
    gps_location_service: GPSLocationService = Depends(get_gps_location_service),
) -> GetGPSLastLocationsUseCase:
    """
    Use case factory for getting gps last locations
    """
    return GetGPSLastLocationsUseCaseImpl(gps_location_service)
