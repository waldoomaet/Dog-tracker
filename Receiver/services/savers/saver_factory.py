from enum import Enum
from services.config_service import ConfigService
from services.savers.saver_base import Saver
from services.savers.tiny_db_saver import TinyDbSaver


class SaverType(Enum):
    TINY_DB_SAVER = 0

class SaverFactory:
    @staticmethod
    def fabricate(type: SaverType) -> Saver:
        config = ConfigService()
        if type == SaverType.TINY_DB_SAVER:
            return TinyDbSaver(config["tiny_db_saver"]["path"])
        else:
            raise Exception("Unknown saver type")