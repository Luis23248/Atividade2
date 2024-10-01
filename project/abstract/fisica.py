from project.abstract.pessoa import Pessoa
from project.models import Endereco
from project.models.enums import Sexo
from project.models.enums import Estado_Civil
from abc import ABC, abstractmethod


class Fisica(ABC,Pessoa):

    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    


    def __str__(self) -> str:
        return(
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone:{self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}"
            f"\nSexo: {self.sexo}"
            f"\nEstado Civil: {self.estadoCivil}"
            f"\nData de nascimento: {self.dataNascimento}"

        )    
