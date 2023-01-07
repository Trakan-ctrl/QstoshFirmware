from collections import defaultdict
from threading import Thread
from typing import Callable
import json
import logging
from src.configs import ConfigParser
from .bluetooth_server import BluetoothServer, ConnectionClosed, SocketClosed
from .messages import is_message_valid

logger = logging.getLogger("connection_broker")

class ConnectionBroker:
    def __init__(self):
        self.server = BluetoothServer()
        self.callbacks = defaultdict(list)
        self.on_client_connected: Callable = None
        self._broker_thread: Thread = Thread(target=self._broker_thread_method)
        self._running = True

    def init_config(self, config: ConfigParser):
        self.server.init_config(config)

    def add_callback_to_topic(self, topic: str, callback: Callable[[dict], None]):
        self.callbacks[topic].append(callback)

    def start_broker(self):
        self._running = True
        self._broker_thread.start()

    def _broker_thread_method(self):
        try:
            self.server.advertise_server()
            self.server.accept_connection()
            if self.on_client_connected:
                self.on_client_connected()
            while self._running:
                data = self.server.recv()
                if data:
                    try:
                        json_data = json.loads(data.decode())
                    except Exception as e:
                        json_data = None
                        logger.warning("Could not parse message: {}, reason: {} -> {}".format(data, type(e), e))
                    if is_message_valid(json_data):
                        print(json_data)
                        if json_data["type"] not in self.callbacks:
                            print("No callback for topic:", json_data["type"])
                        for callback in self.callbacks[json_data["type"]]:
                            callback(json_data)
        except (SocketClosed, ConnectionClosed):
            logger.info("Socket or connection closed")
            self.server.close()
        except Exception as e:
            logger.error(type(e), e)

    def send(self, data: str):
        self.server.send(data.encode())

    def stop_broker(self):
        self._running=False
        self.server.close()
        self._broker_thread.join()
