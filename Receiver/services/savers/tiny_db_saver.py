from pathlib import Path
from typing import Any
from tinydb import TinyDB
from services.savers.saver_base import Saver


class TinyDbSaver(Saver):
    _db = None
    def __init__(self, db_file_path: str) -> None:
        # file = Path(db_file_path)
        # file.mkdir(parents=True, exist_ok=True)
        # self._db = TinyDB(file.absolute().__str__())
        self._db = TinyDB(db_file_path)

    def insert(self, data: dict) -> None:
        self._db.insert(data)