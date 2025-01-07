from abc import ABC, abstractmethod
from dataclasses import dataclass


class Interactor(ABC):
    @dataclass
    class Input(ABC):
        pass

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def _execute(self):
        pass

    def run(self):
        self.validate()
        return self._execute()
