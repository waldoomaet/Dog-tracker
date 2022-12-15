from typing import List
from services.savers.saver_base import Saver
from services.savers.saver_factory import SaverFactory, SaverType


class SaverManager(Saver):
    _savers: List[Saver] = []

    def add(self, type: SaverType) -> None:
        self._savers.append(SaverFactory().fabricate(type))

    def insert(self, data: dict) -> None:
        for saver in self._savers:
            saver.insert(data)
