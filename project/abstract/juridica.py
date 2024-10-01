from project.abstract.pessoa import Pessoa
from project.models import Endereco
from abc import ABC, abstractmethod



class Juridica(ABC, Pessoa):

    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual