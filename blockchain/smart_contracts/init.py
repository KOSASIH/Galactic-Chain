from abc import ABC, abstractmethod

class SmartContract(ABC):
    @abstractmethod
    def deploy(self):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_balance(self, address):
        pass

    @abstractmethod
    def get_owner(self):
        pass
