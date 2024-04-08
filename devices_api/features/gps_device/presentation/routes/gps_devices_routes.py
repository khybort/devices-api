"""
    GPS Devices routes
"""
from devices_api.features.gps_device.presentation.routes import router
from devices_api.features.gps_device.presentation.routes.get_gps_last_locations_route import get_gps_last_locations
from devices_api.features.gps_device.presentation.routes.get_gps_device_locations_route import get_gps_device_locations
from devices_api.features.gps_device.presentation.routes.create_gps_device_route import create_gps_device
from devices_api.features.gps_device.presentation.routes.get_gps_devices_route import get_gps_devices
from devices_api.features.gps_device.presentation.routes.delete_gps_device_route import delete_gps_device


gps_devices_router = router