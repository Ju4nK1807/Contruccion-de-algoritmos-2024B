__author__ = "Juan Camilo Bastidas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "Juan.bastidaspa@campusucc.edu.co"

from Fecha import Fecha 

class Empleado:
    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    nombre = ""
    apellido = ""
    salario = 0
    
    """#----------------------------------------------------------------
    # 1 = Masculino, 2 = Femenino
    ----------------------------------------------------------------#"""
    
    sexo = 0 
    
    """#----------------------------------------------------------------
    # Asociación
    ----------------------------------------------------------------#"""
    
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha() 
    
    """#----------------------------------------------------------------
    # Metodos  
    ----------------------------------------------------------------#"""
    # Este metodo retorna el nombre del empleado
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre
    
    __method__= "CambiarSalario"
    __parameter__= "nuevoSalario"
    __returns__= "Salario"
    __Description__= "metodo que actualiza el salario del empleado" 
  
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo
        self.salario = nuevoSalario
        
    # Retorna el salario del empleado    
    def DarSalario(self):          
          # Aqui va mi codigo
        return self.salario
    
    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.Darfecha() 
    __method__= "CalcularSalarioAnual"
    __parameter__= "Ninguno"
    __returns__= "Salario Anual"
    __Description__= "Muestra el salario anual del  empleado" 
    
    def CalcularSalarioAnual(self): 
        # Aqui va mi codigo
        # forma 1
        # total = self.salario.12
        # return total
        # forma 2
        return self.salario * 12
    
    __method__= "CalcularImpuestoAnual"
    __parameter__= "Ninguno"
    __returns__= "Impuesto del salario Anual"
    __Description__= "Muestra el impuesto del salario anual del  empleado"  
    def CalcularImpuestoAnaul(self):
        # Aqui va mi codigo
        # forma 1
        # SalarioAnual=self.CalcularSalarioAnual ()
        # ImpuestoAnual=SalarioAnual*0.19
        # return ImpuestoAnual
        # forma 2
        return self.CalcularSalarioAnual() * 0.19
    
    __method__= "CalcularImpuestoMensual"
    __parameter__= "Ninguno"
    __returns__= "Impuesto del salario Mensual"
    __Description__= "Muestra el impuesto del salario Mensual del  empleado"  
    def CalcularImpuuestoMensual (self):
        # Aqui va mi codigo
        return self.DarSalario()*0.19
