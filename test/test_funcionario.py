import pytest
from project.models import Funcionario
from project.models.enums import Setor


@pytest.fixture

def funcionario_valido():
    
    return funcionario