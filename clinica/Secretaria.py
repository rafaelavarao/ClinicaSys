from .Pessoa import Pessoa
from . import database

class Secretaria(Pessoa):
    def __init__(self, fullname, cpf, birthday, ec) -> None:
        super().__init__(fullname, cpf, birthday, ec)
        self.func_list = []

    def registrarDados(self):
        # print("Secretária registrada com sucesso!")
        # database.write_funcionarios(str(self)+'\n')
        pass
    
    def obterDados(self):
        # print("Dados da Secretária obtidos com sucesso!")
        database.read_funcionarios()

    def cadastrarFuncionario(self, func):
        # print("Funcionário {} cadastrado com sucesso!".format(str(func)), type(func))
        self.func_list.append(func)

    def __enter__(self):
        # print ('instanciando secretaria', str(self))
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        funcs = []
        for func in self.func_list:
            funcs.append(str(func))
        
        data = database.write_funcionarios('\n'.join(funcs)+'\n')
    