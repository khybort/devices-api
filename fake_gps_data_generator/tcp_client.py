import socket
import time

from logger import Logger

logger = Logger(__name__, 'tcp_client.log')

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # initial socket handshake
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_command(self, command):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.socket.sendall(command.encode('utf-8'))
            response = self.socket.recv(1024)
            time.sleep(3)
            return response.decode('utf-8')
        except Exception as e:
            logger.critical(f"TCP client error: {e}")
            raise e
        finally:
            self.close()

    def close(self):
        self.socket.close()