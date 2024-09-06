from abc import ABC, abstractmethod

class LoggingManager(ABC):
    @abstractmethod
    def info():
        pass

    @abstractmethod
    def pipe():
        pass


