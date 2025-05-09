from Silla import Silla
from Pasajero import Pasajero

class Avion:
    #------------------------------------------
    # Atributos
    #------------------------------------------
    def __init__(self):
        # Crear la matriz de sillas
        self.__sillas = []
        
        # Crear sillas ejecutivas (1-8)
        for i in range(1, 9):
            # Definir ubicación:
            # - Ventana: sillas 1, 4, 5, 8
            # - Pasillo: sillas 2, 3, 6, 7
            if i in [1, 4, 5, 8]:
                ubicacion = Silla.Ubicacion.VENTANA
            else:
                ubicacion = Silla.Ubicacion.PASILLO
            
            self.__sillas.append(Silla(i, Silla.Clase.EJECUTIVA, ubicacion))
        
        # Crear sillas económicas (9-50)
        # 7 filas con 6 sillas cada una (2 ventanas, 2 centros, 2 pasillos por fila)
        for i in range(9, 51):
            posicion = (i - 9) % 6 + 1
            
            # Definir ubicación basada en la posición en la fila:
            # - Ventana: posiciones 1 y 6
            # - Centro: posiciones 2 y 5
            # - Pasillo: posiciones 3 y 4
            if posicion in [1, 6]:
                ubicacion = Silla.Ubicacion.VENTANA
            elif posicion in [2, 5]:
                ubicacion = Silla.Ubicacion.CENTRO
            else:  # posiciones 3 y 4
                ubicacion = Silla.Ubicacion.PASILLO
            
            # Crear y añadir la silla económica
            self.__sillas.append(Silla(i, Silla.Clase.ECONOMICA, ubicacion))
    
    #------------------------------------------
    # Métodos del Taller clase 2
    #------------------------------------------
    
    # 1. Contar sillas ejecutivas ocupadas
    def contarSillasEjecutivasOcupadas(self):
        contador = 0
        for i in range(8):
            if self.__sillas[i].sillaAsignada():
                contador += 1
        return contador
    
    # 2. Buscar pasajero ejecutivo por cédula
    def buscarPasajeroEjecutivo(self, pCedula):
        for i in range(8):
            silla = self.__sillas[i]
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == pCedula:
                return silla
        return None
    
    # 3. Buscar silla económica libre según ubicación
    def buscarSillaEconomicaLibre(self, pUbicacion):
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == pUbicacion:
                return silla
        return None
    
    # 4. Asignar silla económica
    def asignarSillaEconomica(self, pUbicacion, pPasajero):
        silla = self.buscarSillaEconomicaLibre(pUbicacion)
        if silla is not None:
            silla.asignarPasajero(pPasajero)
            return True
        return False
    
    # 5. Anular reserva ejecutivo
    def anularReservaEjecutivo(self, pCedula):
        silla = self.buscarPasajeroEjecutivo(pCedula)
        if silla is not None:
            silla.desasignarSilla()
            return True
        return False
    
    # 6. Contar ventanas económicas disponibles
    def contarVentanasEconomica(self):
        contador = 0
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == Silla.Ubicacion.VENTANA:
                contador += 1
        return contador
    
    # 7. Buscar homónimos en clase económica
    def hayDosHomonimosEconomica(self):
        nombres = []
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if silla.sillaAsignada():
                nombre = silla.darPasajero().darNombre()
                # Si el nombre ya está en la lista, hay homónimos
                if nombre in nombres:
                    return True
                # Agregar el nombre a la lista
                nombres.append(nombre)
        return False
    
    #------------------------------------------
    # Métodos de la Tarea casa 3
    #------------------------------------------
    
    # 1. Contar sillas económicas libres
    def contarSillasEconomicasLibres(self):
        contador = 0
        for i in range(8, len(self.__sillas)):
            if not self.__sillas[i].sillaAsignada():
                contador += 1
        return contador
    
    # 2. Contar pasillos ejecutivos disponibles
    def contarPasilloEjecutivas(self):
        contador = 0
        for i in range(8):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == Silla.Ubicacion.PASILLO:
                contador += 1
        return contador
    
    # 3. Desocupar avión
    def desocuparAvion(self):
        for i in range(len(self.__sillas)):
            self.__sillas[i].desasignarSilla()
