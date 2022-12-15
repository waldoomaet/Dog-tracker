from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def insert(self, data: dict):
        pass