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
        self._broker_thread.start()

    def _broker_thread_method(self):
        try:
            while self._running:
                data = self.server.recv()
                try:
                    json_data = json.loads(data.decode())
                except:
                    json_data = None
                    logger.warning("Could not parse message: {}".format(data))
                if is_message_valid(json_data):
                    for callback in self.callbacks[json_data["topic"]]:
                        callback(json_data)
        except (SocketClosed, ConnectionClosed):
            logger.info("Socket or connection closed")
            self.server.close()
        except Exception as e:
            logger.error(type(e), e)

    def stop_broker(self):
        pass
        #self._broker_thread.
