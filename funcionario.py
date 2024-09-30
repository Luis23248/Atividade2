from my_project.models.enums import setor



class Funcionario:

    def __init__(self, cpf: str, rg: str, matricula: str, setor: setor, salario: float) -> None:
        
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario