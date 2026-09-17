class Fila:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)

    def atender(self):
        if len(self.estudiantes) == 0:
            return None
        return self.estudiantes.pop(0)

    def siguiente(self):
        if len(self.estudiantes) == 0:
            return None
        return self.estudiantes[0]

    def listar(self):
        return self.estudiantes

    def cantidad(self):
        return len(self.estudiantes)

    def esta_vacia(self):
        return len(self.estudiantes) == 0