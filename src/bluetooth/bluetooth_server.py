from threading import Thread
from typing import Callable
from src.configs import ConfigParser, BluetoothConfig
from bluetooth import BluetoothSocket
import bluetooth


class ConnectionClosed(Exception):
    pass

class SocketClosed(Exception):
    pass

class BluetoothServer:
    def __init__(self):
        self.server_socket: BluetoothSocket = BluetoothSocket(bluetooth.RFCOMM)
        self.uuid: str                      = None
        self.timeout: int                   = None
        self.port: int                      = None
        self.bt_settings: BluetoothConfig   = None
        self.client_socket: BluetoothSocket = None
        self.client_info: tuple             = None

    def init_config(self, config: ConfigParser):
        self.bt_settings = config.get_bluetooth_config()
        self.uuid = self.bt_settings.uuid
        self.timeout = self.bt_settings.timeout 
        

    def advertise_server(self):
        self.server_socket.bind(("", bluetooth.PORT_ANY))
        self.server_socket.listen(1)
        self.port = self.server_socket.getsockname()[1]
        bluetooth.advertise_service(
            self.server_socket,
            self.bt_settings.server_name,
            service_id=self.uuid,
            service_classes=[self.uuid, bluetooth.SERIAL_PORT_CLASS],
            profiles=[bluetooth.SERIAL_PORT_PROFILE]
        )

    def accept_connection(self):
        self.client_socket, self.client_info = self.server_socket.accept()
        #self.client_socket.settimeout(self.timeout)

    def recv(self, numbytes: int = 1024):
        try:
            data = self.client_socket.recv(numbytes)
            if not data:
                raise ConnectionClosed()
            return data
        except OSError:
            raise SocketClosed()

    def send(self, data: bytes):
        self.client_socket.send(data)

    def close(self):
        self.server_socket.close()
        self.client_socket.close()
