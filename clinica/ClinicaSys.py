from . import Paciente
from . import Enfermeira
from . import Pessoa
from . import Medico
from . import Secretaria
from . import erros
from . import Convenio


#fazendo uma simplificação pra deixar o codigo mais legivel
Paciente = Paciente.Paciente #paciente recebe o paciente paciente.py e assim a classe paciente 
Enfermeira = Enfermeira.Enfermeira
Pessoa = Pessoa.Pessoa
Medico = Medico.Medico
Secretaria = Secretaria.Secretaria
Convenio = Convenio.Convenio


def parse(file, error): #metodo que separa os dados do arquivo
    lineup = {
        'Medico' : None,
        'Enfermeira' : None,
        'Secretaria': None
        }

    with open(file, 'r') as f: #abre o arquivo e faz split nele
        lines = f.read().split('\n')
        for i, line in enumerate(lines):
            try:
                if line == '': #se a linha for vazia para
                    break

                #"Paciente1__Marcio Lisboa:94874091067:10/09/2001:Solteiro:Unimed:10000" splitando as linhas com "__" e ":"
                cargo, info = line.split('__')
                info = info.split(':')

                #pega as informações de cada linha por indice
                if 'Medico' in cargo:
                    lineup['Medico'] = Medico(info[0], info[1], info[2], info[3], info[4])
                if 'Enfermeira' in cargo:
                    lineup['Enfermeira'] = Enfermeira(info[0], info[1], info[2], info[3], info[4])
                if 'Paciente' in cargo:
                    c = Convenio(info[4], int(info[5])) #pega tipo de convenio e credito do paciente 
                    lineup[cargo] = Paciente(info[0], info[1], info[2], info[3], c)
                if 'Secretaria' in cargo:
                    lineup['Secretaria'] = (info[0], info[1], info[2], info[3])
            except erros.ClinicaException as e: #escreve os erros no erros.txt
                error.write(str(e)+'\n')


        ops = [] 

        # pegando as operações dos funcionarios
        #cmd é a operação, arg é o argumento da operação e descr é a descrição da doença do paciente
        for line in lines[i+1:]: 
            if len(line) == 0: continue
            cargo, op = line.split('=')
            cmd, arg = op.split('->')
            descr = None

            if ':' in arg:
                arg, descr = arg.split(':')

            ops.append((cargo, cmd, arg, descr))

        return lineup, ops