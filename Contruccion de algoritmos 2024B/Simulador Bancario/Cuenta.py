__author__ = "Juan Camilo Bastidas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "Juan.bastidaspa@campusucc.edu.co"

from Cuenta_ahorros import cuenta_ahorros
from Cuenta_cdt import Cuenta_cdt
from Cuenta_corriente import cuenta_Corriente

class cuenta:

    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    __nombre = ""
    __apellido = ""
    __Cedula = ""
    __MesActual= 0
    
    """#----------------------------------------------------------------
    # Asociacion 
    ----------------------------------------------------------------#"""
    
    __CuentaAhorros = cuenta_ahorros ()
    __CuentaCorriente = cuenta_Corriente ()
    __CuentaCDT = Cuenta_cdt ()
    
    """#----------------------------------------------------------------
    # Metodos  
    ----------------------------------------------------------------#"""
    __method__= "DepositarCuentaCorriente"
    __parameter__= "Monto"
    __returns__= "Ninguno"
    __Description__= "Metodo que permite depositar en la cuenta corriente"
    
    def DepositarCuentaCorriente(self, Monto):
        # Aqui va mi codigo
        self.__CuentaCorriente.ConsignarSaldo(Monto)
    
    __method__= "DarSaldoTotal"
    __parameter__= "SaldoTotal"
    __returns__= "Ninguno"
    __Description__= "Metodo que muestra el SaldoTotal"
    
    def DarSaldoTota(self):
        # Aqui va mi codigo
        return self.__CuentaAhorros.DarSaldo+"/"+self.__CuentaCorriente.DarSaldo+"/"+self.__CuentaCDT.DarSaldo
    
    __method__= "DarSaldoCuentaCorriente"
    __parameter__= "Ninguno"
    __returns__= "SaldoCuentaCorriente"
    __Description__= "Metodo que Permite retornar el saldo de la CuenraCorriente"
    
    def DarSaldoCorriente(self):
        return self.__CuentaCorriente.DarSaldo()
    
    __method__= "PasarAhoorroaCorriente"
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__= "Metodo que Permite pasar saldo de la cuentaAhorros a la CuenraCorriente"
    
    def PasarAhoorroaCorriente(self):
    # Aqui va mi codigo
      SaldoAhorros = self.__CuentaAhorros.DarSaldo()
      self.__CuentaAhorros.RetirarSaldo(SaldoAhorros)
      self.__CuentaCorriente.ConsignarSaldo(SaldoAhorros)
    
    __method__= "PasarCorrienteaAhorros"
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__= "Metodo que Permite pasar saldo de la CuentaCorriente a la CuentaAhorros"
    
    def Ahorrar(self, monto):
    # Aqui va mi codigo
     SaldoCorriente = self.__CuentaCorriente(monto)
     self.__CuentaCorriente.RetirarSaldo(SaldoCorriente)
     self.__CuentaAhorros.ConsignarSaldo(SaldoCorriente)
     
    __method__= "retirarAhorro"
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__= "Metodo que Permite Retirar un monto de la cuenta ahorros"
    
    def retirarAhorro(self, monto):     
    # Aqui va mi codigo 
     SaldoAhorros = self.__CuentaAhorros(monto)
     self.__CuentaAhorros.RetirarSaldo(monto)
     
    __method__= "retirarTodo"
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__= "Metodo que Permite Retirar un Todo"
    
    def retirarTodo(self):
     # Aqui va mi codigo
     self.__CuentaAhorros.RetirarSaldo(self.__CuentaAhorros.DarSaldo())
     self.__CuentaCorriente.RetirarSaldo(self.__CuentaCorriente.DarSaldo())
    
    __method__= "duplicarAhorro"
    __parameter__= "Ninguno"
    __returns__= "Ninguno"
    __Description__= "Metodo que Permite Duplicar el dinero de la CuentaAhorro"
    
    def duplicarAhorro(self):
     # Aqui va mi codigo
     self.__CuentaAhorros.ConsignarValor(self.__CuentaAhorros.DarSaldo())
     