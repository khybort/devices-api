import pytest
from tests.conftest import client

@pytest.fixture
def gps_device():
    response = client.post("/api/v1/gps-devices", json={"name": "gps_tester"})
    yield response.json()
    client.delete(f"/api/v1/gps-devices/{response.json()['id']}")
    


class TestGPSDevices:
    def test_create_gps_device(self):
        payload = {
            "name": "tester"
        }
        response = client.post("/api/v1/gps-devices", json=payload)
        assert response.status_code == 201
        assert response.json()['name'] == payload['name']
    
    @pytest.mark.usefixtures("gps_device")
    def test_get_gps_devices(self):
        response = client.get("/api/v1/gps-devices")
        assert response.status_code == 200
        assert len(response.json()) > 0
    
    @pytest.mark.usefixtures("gps_device")
    def test_delete_gps_device(self, gps_device):
        response = client.delete(f"/api/v1/gps-devices/{gps_device['id']}")
        assert response.status_code == 200
        assert response.json()['name'] == gps_device['name']
        assert response.json()['is_deleted'] == True
    
