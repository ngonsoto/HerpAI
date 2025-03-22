import json
import logging
import time
import threading
import pika  # or redis/kafka depending on your broker
from agents.document_tagging_agent import DocumentTaggingAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TaggingWorker")

BROKER_URL = "amqp://guest:guest@localhost:5672/"  # Update as needed
QUEUE_NAME = "document_tagging"


def on_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        event_type = message.get("event")

        if event_type == "DOCUMENT_INGESTION_COMPLETED":
            logger.info("[Worker] Received ingestion completion event. Starting tagging...")
            agent = DocumentTaggingAgent()
            result = agent.run()
            logger.info(f"[Worker] Tagging Completed: {result}")
        else:
            logger.warning(f"[Worker] Ignored unknown event: {event_type}")
    except Exception as e:
        logger.error(f"[Worker] Error processing message: {e}")


def start_worker():
    connection = pika.BlockingConnection(pika.URLParameters(BROKER_URL))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    logger.info("[Worker] Waiting for ingestion events...")
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    start_worker()
