from statistics import mean

class Estudiante:
    def __init__(self, dni: str, nombre: str, grupo: str) -> None:
        self.dni = dni
        self.nombre = nombre
        self.grupo = grupo
        self.notas = {}

    def matricula(self, asignatura) -> bool:
        if asignatura in self.notas:
            return False
        else:
            self.notas[asignatura] = []
            return True
        
    def ponerNota(self, asignatura: str, nota: float):
        if asignatura in self.notas:
            self.notas[asignatura].append(nota)
            return True
        else:
            return False
    
    def notaMedia(self, asignatura: str):
        if asignatura not in self.notas or len(self.notas[asignatura]) == 0:
            return None
        
        return mean(self.notas[asignatura])
    
    def asignaturas(self):
        return self.notas.keys()
    
# ------- programa --------

PROGRAMACION = "PRG"
ALGORITMOS = "ALG"

estudiante = Estudiante("12345678z", "Juanito Valderrama", "studio")
estudiante.matricula(PROGRAMACION)
estudiante.matricula(ALGORITMOS)

estudiante.ponerNota(PROGRAMACION, 8.0)
estudiante.ponerNota(PROGRAMACION, 9.0)
estudiante.ponerNota(PROGRAMACION, 7.0)

estudiante.ponerNota(ALGORITMOS, 5.0)
estudiante.ponerNota(ALGORITMOS, 6.0)
estudiante.ponerNota(ALGORITMOS, 7.4)

for asignatura in estudiante.asignaturas():
    notaMedia = estudiante.notaMedia(asignatura)
    print(f'{asignatura}: {notaMedia:.2f}')