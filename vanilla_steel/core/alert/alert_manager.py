from abc import ABC, abstractmethod

class AlertManager(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def dismiss():
        pass
    
    @abstractmethod
    def notify():
        pass


    