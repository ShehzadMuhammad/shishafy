from abc import ABC, abstractmethod
from dataclasses import dataclass


class Interactor(ABC):
    @dataclass
    class Input(ABC):
        pass

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def _clean(self):
        pass

    @abstractmethod
    def _validate(self):
        pass

    @abstractmethod
    def _execute(self):
        pass

    def run(self):
        self._clean()
        self._validate()
        return self._execute()
