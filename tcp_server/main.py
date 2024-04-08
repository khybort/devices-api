import pika
import socket
import os


from logger import Logger

logger = Logger(__name__, 'tcp_server.log')

TCP_SERVER_HOST = os.getenv("TCP_SERVER_HOST")
TCP_SERVER_PORT = int(os.getenv("TCP_SERVER_PORT"))
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))

def process_request(client_socket, rabbitmq_channel):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            logger.info(f"Received data from client: {data}")
            device_id, lat, long = data.split(':')
            response = rabbitmq_channel.basic_publish(
                    exchange='',  # default exchange, as we cannot publish directly to a queue in rabbitmq
                    routing_key='gps_data-db-writer',
                    body=f'{device_id}:{lat}:{long}'
                )
            logger.info(f"Sent response to client: {response}")
            
            response_byte_str = str(response).encode('utf-8') if response and not isinstance(response, bytes) else response 

            client_socket.send(response_byte_str if response_byte_str else b'0')


    except Exception as e:
        logger.error(f"Error handling client request: {e}")

    finally:
        client_socket.close()

def start_tcp_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind((TCP_SERVER_HOST, TCP_SERVER_PORT))
        server_socket.listen(5)

        logger.info(f"Listening on {TCP_SERVER_HOST}:{TCP_SERVER_PORT}")

        while True:
            logger.info("Waiting for connection...")
            rabbitmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672))
            rabbitmq_channel = rabbitmq_conn.channel()
            rabbitmq_channel.queue_declare(queue='gps_data-db-writer')
            client_socket, addr = server_socket.accept()
            logger.info(f"Accepted connection from {addr[0]}:{addr[1]}")

            process_request(client_socket, rabbitmq_channel)

    except Exception as e:
        logger.critical(f"TCP server error: {e}")
        server_socket.close()

    except KeyboardInterrupt:
        logger.info("Shutting down the server")
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()
