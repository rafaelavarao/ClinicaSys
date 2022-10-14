from abc import ABC, abstractmethod
from . import database

from . import erros

class Pessoa(ABC):
    def __init__(self, fullname, cpf, birthday, ec) -> None:
        erros.check_cpf(cpf)
        erros.check_bf(birthday)
        erros.check_ec(ec)
        self.full_name = fullname
        self.cpf = cpf
        self.birthday = birthday
        self.ec = ec

    @abstractmethod
    def registrarDados(self):
        pass

    @abstractmethod
    def obterDados(self):
        pass

    def __str__(self):
        return "||".join([self.full_name, self.cpf, self.birthday, self.ec])
