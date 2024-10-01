from project.abstract.juridica import Juridica
from project.models import Endereco


class PrestacaoServico(Juridica):


    def __init__(self, id: str, nome: str, telefone: int, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio: str, contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
    
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim






