__author__ = "Juan Camilo Bastidas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "Juan.bastidaspa@campusucc.edu.co"

class cuenta_ahorros:

    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    __Saldo = 0
    __Interes = 0

    """#----------------------------------------------------------------
    # Metodos  
    ----------------------------------------------------------------#"""
    __method__= "DarSaldo"
    __parameter__= "Ninguno"
    __returns__= "Saldo"
    __Description__=  "Metodo que muestra el saldo del cliente"
    
    def DarSaldo(self):
    # Aqui va mi codigo
        return self.__Saldo 
    
    __method__= "ConsignarValor"
    __parameter__= "Monto"
    __returns__= "Ninguno"
    __Description__= "Metodo para consignar Monto a la cuenta corriente"
    
    def ConsignarValor(self, Monto):
    # Aqui va mi codigo
        self.__Saldo = self.__Saldo+Monto
        
    __method__= "RetirarValor"
    __parameter__= "Monto"
    __returns__= "Ninguno"
    __Description__=  "Metodo para retirar monto de la cuenta corriente"    
    
    def RetirarValor(self, Monto):
    # Aqui va mi codigo
        self.Saldo = self.__Saldo - Monto           