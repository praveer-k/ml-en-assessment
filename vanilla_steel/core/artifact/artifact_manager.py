from abc import ABC, abstractmethod

class ArtifactManager(ABC):
    @abstractmethod
    def upload():
        pass

    @abstractmethod
    def download():
        pass
    
    @abstractmethod
    def verify():
        pass

    @abstractmethod
    def delete():
        pass

    