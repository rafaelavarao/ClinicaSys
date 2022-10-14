from .Pessoa import Pessoa
from . import database
from . import erros

class Medico(Pessoa):
    def __init__(self, fullname, cpf, birthday, ec, crm) -> None:
        super().__init__(fullname, cpf, birthday, ec)
        crm = crm.split(' ')[1]
        erros.check_crm(crm)
        self.crm = crm.upper()

    def registrarDados(self):
        print("Médico registrado com sucesso!")

    def obterDados(self):
        print("Dados do médico obtidos com sucesso!")
        return database.read_funcionarios()

    def __str__(self) -> str:
        return super().__str__() + f"||CRM/RS {self.crm}" 
    
    def internar(self, paciente):
        # print ('internando paciente: ', paciente.full_name)
        paciente.statusInternacao = "Internado"

    def liberar(self, paciente):
        # print ('liberando paciente: ', paciente.full_name)
        if paciente.statusInternacao is None:
            raise ValueError('Paciente não foi internado!')
        paciente.statusInternacao = "Liberado"

    def diagnosticar(self, paciente, problema):
        paciente.problema = problema

if __name__ == "__main__":
    with Medico("João", "123456789", "01/01/2000", "Solteiro", "CRM/RS 123456") as m:
        m.registrarDados()
        m.internar()
        m.diagnosticar()

        pass