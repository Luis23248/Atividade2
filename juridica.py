from pessoa import Pessoa
from my_project.models import Endereco
from my_project.models.enums import Sexo
from my_project.models.enums import Estado_Civil



class Juridica(Pessoa):

    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual