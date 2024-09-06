from abc import ABC, abstractmethod

class PaymentManager(ABC):
    @abstractmethod
    def transact():
        pass

    @abstractmethod
    def reconcile():
        pass

    @abstractmethod
    def settle():
        pass


class PaymentGateway(PaymentManager):
    pass

class DigitalWallet(PaymentManager):
    pass

class PointOfSale(PaymentManager):
    pass

class Subscription(PaymentManager):
    pass

class Cryptocurrency(PaymentManager):
    pass

class BankTransfer(PaymentManager):
    pass

class MobilePayment(PaymentManager):
    pass

class CardPayment(PaymentManager):
    pass