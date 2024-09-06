from abc import ABC, abstractmethod

class OrderManager(ABC):
    @abstractmethod
    def create_order():
        pass

    @abstractmethod
    def track_order():
        pass

    @abstractmethod
    def settle_payment():
        pass

    @abstractmethod
    def return_order():
        pass




