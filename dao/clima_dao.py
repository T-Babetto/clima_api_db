from abc import ABC, abstractmethod


class ClimaDao(ABC):

    @abstractmethod
    def adicionar(self, clima):
        pass

    @abstractmethod
    def selecionar_clima(self, limit=10) -> list:
        pass

    @abstractmethod
    def excluir(self, id):
        pass

    @abstractmethod
    def buscar_clima_hoje(self):
        pass
