from my_project.models.enums import unidadeFederativa


class Endereco:

    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: unidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
        self.numero = numero
        self.uf = uf


    def __str__(self) -> str:
        return(
            f"\n"
        )    