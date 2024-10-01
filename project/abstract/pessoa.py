from project.models import Endereco
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self,id: str, nome: str, telefone: int, email: str, endereco: Endereco) -> None:
        
        self.id = id
        self._nome = nome
        self._idade = telefone
        self._sexo = email
        self.endereco = endereco
    



    def __str__(self) -> str:
        return (
            f"\nID: {self._id}"
            f"\nNome: {self._nome}"
            f"\nTelefone: {self._telefone}"
            f"\nE-mail: {self._email}"
            f"\nEndereço: {self._endereco}"
        )