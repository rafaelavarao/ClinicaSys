from clinica import ClinicaSys

def main(file, error):
    lineup, ops = ClinicaSys.parse(file, error)

    sec_info = lineup['Secretaria']
    with ClinicaSys.Secretaria(sec_info[0], sec_info[1], sec_info[2], sec_info[3]) as sec:
        lineup['Secretaria'] = sec
        for cargo, cmd, arg, descr in ops:
            try:
                if cargo == 'Secretaria':
                    if cmd == 'cadastrar':
                        sec.cadastrarFuncionario(lineup[arg])

                if cargo == 'Medico':
                    if cmd == 'diagnosticar':
                        lineup['Medico'].diagnosticar(lineup[arg], descr)
                    if cmd == 'internar':
                        lineup['Medico'].internar(lineup[arg])
                    if cmd == 'liberar':
                        lineup['Medico'].liberar(lineup[arg])

                if cargo == 'Enfermeira':
                    if cmd == 'cadastrar':
                        lineup['Enfermeira'].cadastrarPaciente(lineup[arg])
                    if cmd == 'relatorio':
                        lineup['Enfermeira'].gerarRelatorio(lineup['Medico'], lineup[arg])
                
            except Exception as e:
                error.write('Não é possivel realizar a operação {} do cargo {} com o argumento {} e descrição {} \n'.format(cmd, cargo, arg, descr))
        
        lineup['Enfermeira'].registrarDados()

if __name__ == '__main__':
    import os
    import sys

    if not os.path.exists('errors'):
        os.makedirs('errors')
    
    if not os.path.exists('relatorios'):
        os.makedirs('relatorios')

    for arg in sys.argv[1:]:
        path = os.path.join('operacoes', arg)
        error = open('errors/{}.txt'.format(arg[0]), 'a' )
        main(path, error)
        error.close()

