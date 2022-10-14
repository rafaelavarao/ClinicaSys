import os

dbasepath = 'database'

if not os.path.exists(dbasepath): #cria o caminho 'database' caso não exista
    os.mkdir(dbasepath)



funcpath = os.path.join(dbasepath, 'funcionarios.dat') #cria o caminho 'database/funcionarios.dat'
with open(funcpath, 'w') as f:
    f.write('')

pacientpath = os.path.join(dbasepath, 'pacientes.dat')# cria o caminho 'database/pacientes.dat'
with open(pacientpath, 'w') as f:
    f.write('')



def write_funcionarios(data): #escreve os dados no arquivo funcionarios.dat
    with open(funcpath, 'a') as f:
        f.write(data)

def read_funcionarios(): #le os dados do arquivo funcionarios.dat
    with open(funcpath, 'r') as f:
        return f.read()

def write_pacientes(data):#escreve os dados no arquivo pacientes.dat
    with open(pacientpath, 'a') as f:
        f.write(data)

def read_pacientes():
    with open(pacientpath, 'r') as f:#le os dados do arquivo pacientes.dat
        return f.read()
