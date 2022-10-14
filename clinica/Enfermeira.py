from .Pessoa import Pessoa
from . import database
from datetime import datetime
from . import erros

class Enfermeira(Pessoa):
    def __init__(self, fullname, cpf, birthday, ec, coren) -> None:
        super().__init__(fullname, cpf, birthday, ec)
        self.coren = coren
        erros.check_coren(coren)
        self.pacientes = []

    def registrarDados(self): #metodo que registra dados chamando do database
        for data in self.pacientes:
            database.write_pacientes(str(data)+'\n')

    def obterDados(self):
        return database.read_funcionarios()

    def cadastrarPaciente(self, data): #metodo que cadastra o paciente
        # print("Paciente cadastrado com sucesso!")
        self.pacientes.append(data)

    def __str__(self) -> str: #metodo que printa as informações da enfermeira
        return super().__str__() + f"||{self.coren}"

    def gerarRelatorio(self, Medico, Paciente): #metodo que gera um relatorio 
        relatorio = f'relatorios/rel_{Paciente.cpf}.txt'

        with open(relatorio, 'w') as f: #metodo que escreve as informações do paciente no relatorio
            f.write('Centro de pós-operatório do Hospital São Lucas')
            f.write('\n\n')
            f.write('################################################')
            f.write('\n\n')
            f.write('Data: {}'.format(datetime.now().strftime('%d/%m/%Y')))
            f.write('\n')
            f.write(f'Relatamos que o paciente {Paciente.full_name}, identificado pelo CPF: {Paciente.cpf},')
            f.write('\n')
            f.write(f'foi atendido pelo médico {Medico.full_name}, identificado pela credencial: CRM/RS {Medico.crm}')
            f.write('\n')
            f.write(f'Saldo do Convenio: {Paciente.convenio}')
            f.write('\n')
            f.write(f'Diagnóstico Final: {Paciente.problema}')
    
        
