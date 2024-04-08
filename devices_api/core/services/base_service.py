from abc import ABC, abstractmethod

class BaseService(ABC):
    """
    Abstract Generic Service
    """

    @abstractmethod
    def find_all(self):
        raise NotImplementedError()