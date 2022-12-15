import yaml
from threading import Lock

class ConfigService:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    with open('./config.yaml') as f:
                        cls._instance = yaml.load(f, Loader=yaml.FullLoader)
        return cls._instance