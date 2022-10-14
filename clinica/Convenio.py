from . Paciente import Paciente
from . import database

class Convenio:
    def __init__(self, convenio_type, credito):
        self.convenio_type = convenio_type ## SUS, IPE, unimed
        self.credito = Credito(credito)

#se for sus ele não cobra nada e se o usuario tiver creditos, ele cobra 500 para internar
    def internar(self): 
        if self.convenio_type == 'SUS':
            return True

        if self.credito < 0 or self.credito == 0:
            return False
        
        self.credito = self.credito - 500
        return True

#se for sus ele não cobra nada e se o usuario tiver creditos, ele cobra 150 para diagnosticar
    def diagnosticar(self):
        if self.convenio_type == 'SUS':
            return True

        if self.credito < 0 or self.credito == 0:
            return False
        
        self.credito = self.credito - 150
        return True
    
#retorna o credito
    def __str__(self):
        return "{}-{}".format(self.convenio_type, str(self.credito))

#classe credito que faz as operações matematicas 
class Credito:
    def __init__(self, valor):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor

    def __float__(self):
        return self._valor
    
    def __str__(self):
        return str(self._valor)

    '''Operadores aritméticos'''
    def __add__(self, other):
        return Credito(self._valor + other)

    def __iadd__(self, other):
        self._valor += other
        return Credito(self._valor) 

    def __sub__(self, other):
        return Credito(self._valor - other)

    def __isub__(self, other):
        self._valor -= other
        return Credito(self._valor) 

    def __mul__(self, other):
        return Credito(self._valor * other)

    '''Operadores Logicos'''
    def __lt__(self, other):
        return self._valor < other
    
    def __gt__(self, other):
        return self._valor > other
    
    def __eq__(self, other):
        return self._valor == other
    
    def __ne__(self, other):
        return self._valor != other


if __name__ == "__main__":
    c = Convenio('unimed', 1000)

    print(c.credito)
    c.internar()
    print(c.credito)
    c.diagnosticar()
    print(c.credito)

    # p = Paciente(...., c)