from abc import ABC, abstractmethod
from dataclasses import dataclass


class Interactor(ABC):
    @dataclass
    class Input(ABC):
        pass

    @abstractmethod
    def validate(self, **inputs):
        pass

    @abstractmethod
    def _execute(self, **inputs):
        pass

    def run(self, **inputs):
        self.validate(**inputs)
        return self._execute(**inputs)
