from project.abstract.juridica import Juridica
from project.models import Endereco


class Fornecedor(Juridica):

    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        
        self.produto = produto

        