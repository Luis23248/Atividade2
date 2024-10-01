from project.models.enums import Setor
from abc import ABC, abstractmethod
from project.models import Fisica

class Funcionario(ABC, Fisica):

    def __init__(self, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario