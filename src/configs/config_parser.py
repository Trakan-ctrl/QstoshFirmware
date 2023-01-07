import configparser


class BluetoothConfig:
    def __init__(self, configs):
        self.configs = configs

    @property
    def uuid(self):
        return self.configs["uuid"]

    @property
    def server_name(self):
        return self.configs["server_name"]

    @property
    def timeout(self):
        return int(self.configs["timeout"])

class ConfigParser:
    def __init__(self, filename: str):
        self.parser = configparser.ConfigParser()
        self.parser.read(filename)

    def get_bluetooth_config(self):
        return BluetoothConfig(self.parser["bluetooth"])

