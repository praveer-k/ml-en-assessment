from abc import ABC, abstractmethod

class AuthenticationManager(ABC):
    @abstractmethod
    def authenticate():
        pass
