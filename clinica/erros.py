from curses.ascii import isdigit

class ClinicaException(Exception):
    pass

with open('error.txt', 'w' ) as error:
    pass

#confere se todos os caracteres são digitos e se possuem 11 numeros
def check_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ErroCpf(cpf)

def check_coren(coren):
    if len(coren) != 7 and not coren.isdigit():
        raise ErroCoren(coren)

def check_crm(crm):
    if len(crm) != 6 and not crm.isdigit():
        raise ErroCRM(crm)

def check_ec(ec):
    if ec.lower() != 'solteiro' and ec.lower() != 'casado':
        raise ErroEC(ec)

def check_bf(bf):
    #separa o dia, mes e ano
    dia, mes, ano = bf.split("/")
    erro = 0

    #confere se o dia é existente
    if not dia.isdigit():
        erro = 1
    
    elif int(dia) > 31 or int(dia) < 1:
        erro = 1
    
    #confere se o mes é existente
    elif not mes.isdigit():
        erro = 1
    
    elif int(mes) > 12 or int(mes) < 1:
        erro = 1
    
    #confere se o ano é existente
    elif not ano.isdigit():
        erro = 1
    
    elif int(ano) > 2022 or int(ano) < 1800:
        erro = 1
    
    if erro:
        raise ErroBF(bf)
            


class ErroCpf(ClinicaException):  
    def __init__(self, cpf):
        self._cpf = cpf
    
    def __str__(self):
        s = "ERROR: O CPF possui " + str(len(self._cpf)) + " caracteres CPF precisa ter 11 digitos"
        return s 

#confere se todos os caracteres são digitos e se possuem 7 numeros
class ErroCoren(ClinicaException): 
    def __init__(self, coren):
        self._coren = coren
    
    def __str__(self):
        s = "ERROR: O COREN possui " + str(len(self._coren)) + " caracteres COREN precisa ter 7 digitos"
        return s

#confere se todos os caracteres são digitos e se possuem 6 numeros
class ErroCRM(ClinicaException):
    def __init__(self, crm):
        self._crm = crm
    
    def __str__(self):
        s = "ERROR: O CRM possui " + str(len(self._crm)) + " caracteres CRM precisa ter 6 digitos"
        return s
    
#confere se o estado civil digitado é diferente de solteiro/casado
class ErroEC(ClinicaException): 
    def __init__(self, ec):
        self._ec = ec
    
    def __str__(self):
        s = "ERROR: O Estado Civil " + str(self._ec) + " não encontrado"
        return s
    
#confere se a data de nascimento esta correta     
class ErroBF(ClinicaException): 
    def __init__(self, dn):
        self._dn = dn
    
    def __str__(self):
        dia, mes, ano = self._dn.split("/")
        s = []

        #confere se o dia é existente
        if not dia.isdigit():
            s.append("ERROR: O dia " + str(self._dn) + " não é um número")

        if int(dia) > 31 or int(dia) < 1:
            s.append("ERROR: Dia de nascimento invalido")

        #confere se o mes é existente
        if not mes.isdigit():
            s.append("ERROR: O mes " + str(mes) + " não é um número")

        if int(mes) > 12 or int(mes) < 1:
            s.append("ERROR: Mês inválido")

        #confere se o ano é existente
        if not ano.isdigit():
            s.append("ERROR: O ano " + str(ano) + " não é um número")

        if int(ano) > 2022 or int(ano) < 1800:
            s.append("ERROR: Ano inválido")
        
        return '\n'.join(s)