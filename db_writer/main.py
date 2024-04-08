import pika
import os
import psycopg2
from logger import Logger

logger = Logger(__name__, 'db_writer.log')
pg_conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

def start_consumer():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("RABBITMQ_HOST"), port=os.getenv("RABBITMQ_PORT")))
            channel = connection.channel()

            channel.queue_declare(queue='gps_data-db-writer')

            def callback(ch, method, properties, body):
                logger.info(f"Received data from client: {body}")
                device_id, lat, long = body.decode('utf-8').split(':')
                cur = pg_conn.cursor()
                cur.execute("INSERT INTO locations (device_id, longitude, latitude) VALUES (%s, %s, %s)", (device_id, lat, long))
                pg_conn.commit()
                cur.close()
                ch.basic_ack(delivery_tag = method.delivery_tag)

            # QOS — Quality of Service
            channel.basic_qos(prefetch_count=1)  # process one message at once, won't pull more if not done with processing
            channel.basic_consume(queue='gps_data-db-writer', on_message_callback=callback)

            logger.info(' [*] Waiting for messages.')
            channel.start_consuming()

        # Do not recover if connection was closed by broker
        except pika.exceptions.ConnectionClosedByBroker:
            raise
        # Do not recover on channel errors
        except pika.exceptions.AMQPChannelError:
            raise
        # Recover on all other connection errors
        except pika.exceptions.AMQPConnectionError:
            # other exceptions such as StreamLostError and TimeoutError
            # inherit from AMQPConnectionError
            continue
        except Exception as e:
            logger.critical(f"Error in main: {e}")
            raise


if __name__ == '__main__':
    start_consumer()
