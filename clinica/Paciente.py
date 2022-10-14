from .Pessoa import Pessoa
from . import database
from . import erros

class Paciente(Pessoa):
    def __init__(self, name, cpf, birthday, ec, convenio) -> None:
        super().__init__(name, cpf, birthday, ec)
        self.convenio = convenio
        self.problema = None
        self.statusInternacao = None

    def __str__(self) -> str:
        if self.statusInternacao is not None:
            return super().__str__() + f"||{self.convenio}||{self.problema}||{self.statusInternacao}"
        return super().__str__() + f"||{self.convenio}||{self.problema}"
    
    def obterDados(self):
        return 
    
    def registrarDados(self):
        return
