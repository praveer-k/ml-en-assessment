from abc import ABC, abstractmethod

class JobManager(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def abort():
        pass

    @abstractmethod
    def schedule():
        pass
