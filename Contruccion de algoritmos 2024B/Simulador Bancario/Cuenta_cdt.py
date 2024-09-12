__author__ = "Juan Camilo Bastidas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "Juan.bastidaspa@campusucc.edu.co"

class Cuenta_cdt:

    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    Saldo = 0
    Interes_Banco = 0
    
    """#----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------#"""
    __method__= "ConsignarValor"
    __parameter__= "Ninguno"
    __returns__= "Valor"
    __Description__= "Metodo para consignar valor"
 
 
    def ConsignarValor(self, nuevoValor):
    # Aqui va mi codigo
        self.Saldo = self.Saldo + nuevoValor
     

    __method__= "DarSaldo"
    __parameter__= "Ninguno"
    __returns__= "Saldo"
    __Description__=  "Metodo que retorna el saldo del cliente"

    def DarSaldo(self):
    # Aqui va mi codigo
        return self.Saldo 

    __method__= "RetirarValor"
    __parameter__= "Monto"
    __returns__= "Saldo"
    __Description__=  "Metodo para retirar saldo de la cuenta"
             
    def RetirarValor(self, monto):
    # Aqui va mi codigo
        self.Saldo = self.Saldo - monto
