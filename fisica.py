from pessoa import Pessoa
from my_project.models import Endereco
from my_project.models.enums import Sexo
from my_project.models.enums import Estado_Civil


class Fisica(Pessoa):

    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: Estado_Civil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento




    def __str__(self) -> str:
        return(
            f"\n"
        )    
