__author__ = "Juan Camilo Bastidas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "Juan.bastidaspa@campusucc.edu.co"

class Fecha:
    # Aquí inicia la declaracion de la clase
    
    """#----------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------#"""
    
    Dia = 0
    Mes = 0
    Año = 0
    
    """#----------------------------------------------------------------
    # Metodos  
    ----------------------------------------------------------------#"""
    __method__= "Dardia"
    __parameter__= "Ninguno"
    __returns__= "Dia"
    __Description__= "Metodo que regresa el dia"
 
    def DarDia(self):
        # Aqui va mi codigo
        return self.Dia
    
    __method__= "DarMes"
    __parameter__= "Ninguno"
    __returns__= "Mes"
    __Description__= "Metodo que regresa el Mes"
 
    def CambiarMes(self, nuevoSalario):
        # Aqui va mi codigo
        return self.Mes
    
    __method__= "DarAnio"
    __parameter__= "Ninguno"
    __returns__= "Anio"
    __Description__= "Metodo que regresa el Anio"
 
    def DarAnio(self):          
          # Aqui va mi codigo
        return self.anio

    __method__= "DarFecha"
    __parameter__= "Ninguno"
    __returns__= "Fecha"
    __Description__= "Metodo que regresa la fecha"

    def Darfecha(self):
        return self.dia+"/"+self.Mes+"/"+self.anio
      