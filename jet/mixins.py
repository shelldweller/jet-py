from abc import ABC, abstractmethod
from typing import Any


class Resolvable(ABC):
    @abstractmethod
    def resolve(self, record:dict) -> Any:
        pass
