import random

class Guerrero:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.__vida = 100
        self.fuerza = random.randint(10,100)
        self.precision = random.randint(10,100)
        self.velocidad = random.randint(10,50)
        self.defensa = random.randint(10,70)

    def golpear(self, guerrero):
        if self.__aciertaGolpeContra(guerrero):
            self.__hacerDanyoA(guerrero)
    
    def sigueVivo(self):
        return self.__vida > 0
    
    def recibirDanyo(self, danyo: int):
        print(f'ha recibido {danyo}')
        self.__vida -= danyo

    def mostrarVida(self):
        return f'Guerrero: {self.nombre}\n\
                 Vida: {self.__vida}'
    
    def __aciertaGolpeContra(self, guerrero):
        porcentajePrecision = (self.precision - guerrero.velocidad)/100
        return porcentajePrecision > 0.5
    
    def __hacerDanyoA(self, guerrero):
        cantidadDanyo = max(self.fuerza - guerrero.defensa + random.randrange(-10,11), 1)
        print(f"Cantidad daño:{cantidadDanyo}")

        guerrero.recibirDanyo(cantidadDanyo)

    def __str__(self) -> str:
        return f'Guerrero: {self.nombre}\n\
                 Vida: {self.__vida}\n\
                 Fuerza: {self.fuerza}\n\
                 Precision: {self.precision}\n\
                 Velocidad: {self.velocidad}\n\
                 Defensa: {self.defensa}'



# ---------- Programa -----------
jugador1 = Guerrero('Goku')
jugador2 = Guerrero('Superman')

print(jugador1)
print(jugador2)

atacante = jugador1 if jugador1.velocidad > jugador2.velocidad else jugador2
defensor = jugador1 if jugador1.velocidad <= jugador2.velocidad else jugador2

while atacante.sigueVivo() and defensor.sigueVivo():
    atacante.golpear(defensor)

    print("-- Atacante --")
    print(atacante.mostrarVida())
    
    print("-- Defensor --")
    print(defensor.mostrarVida())

    # Cambia el turno
    atacante, defensor = defensor, atacante

ganador = jugador1 if jugador1.sigueVivo() else jugador2

print(f'El ganador ha sido: {ganador.nombre}')