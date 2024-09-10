from abc import ABC, abstractmethod

class AgentManager(ABC):
    @abstractmethod
    def run():
        pass

    @abstractmethod
    def alert():
        pass
    
    @abstractmethod
    def load_data():
        pass

    @abstractmethod
    def delete():
        pass

    