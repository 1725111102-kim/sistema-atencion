from models.estudiante import Estudiante
from models.fila import Fila

fila = Fila()


def agregar_estudiante(matricula, nombre, carrera, tramite):
    estudiante = Estudiante(matricula, nombre, carrera, tramite)
    fila.agregar(estudiante)


def atender_estudiante():
    return fila.atender()


def ver_siguiente():
    return fila.siguiente()


def ver_fila():
    return fila.listar()


def ver_cantidad():
    return fila.cantidad()


def fila_vacia():
    return fila.esta_vacia()