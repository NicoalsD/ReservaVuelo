class Pasajero:
    #---------------------------
    # Atributos
    #---------------------------
    def __init__(self, pCedula, pNombre):
        self.__cedula = pCedula
        self.__nombre = pNombre
    
    #---------------------------
    # Métodos
    #---------------------------
    def darCedula(self):
        return self.__cedula
    
    def darNombre(self):
        return self.__nombre