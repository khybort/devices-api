import os
from faker import Faker

from logger import Logger
from tcp_client import TCPClient

fake = Faker()
Faker.seed(0)
logger = Logger(__name__, 'fake_gps_data_generator.log')
tcp_client = TCPClient(host=os.getenv("TCP_SERVER_HOST"), port=int(os.getenv("TCP_SERVER_PORT")))

def start_tcp_client():
    try:
        device_id = os.getenv("FAKE_GPS_DEVICE_ID")
        while True:
            latitude = fake.latitude()
            longitude = fake.longitude()
            tcp_client.send_command(f"{device_id}:{latitude}:{longitude}")
            logger.info(f"Sent data to TCP server: {device_id}:{latitude}:{longitude}")
    except Exception as e:
        logger.critical(f"TCP client error: {e}")
if __name__ == "__main__":
    start_tcp_client()
