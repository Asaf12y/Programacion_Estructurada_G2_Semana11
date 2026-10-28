
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    elif valor > raiz.valor:
        raiz.derecha = insertar(raiz.derecha, valor)

    return raiz


def eliminar(raiz, valor):
    if raiz is None:
        return None

    if valor < raiz.valor:
        raiz.izquierda = eliminar(raiz.izquierda, valor)

    elif valor > raiz.valor:
        raiz.derecha = eliminar(raiz.derecha, valor)

    else:
        # Caso 1: hoja o solo hijo derecho
        if raiz.izquierda is None:
            return raiz.derecha

        # Caso 2: solo hijo izquierdo
        if raiz.derecha is None:
            return raiz.izquierda

        # Caso 3: tiene dos hijos
        sucesor = raiz.derecha

        # Buscar el menor del subárbol derecho
        while sucesor.izquierda is not None:
            sucesor = sucesor.izquierda

        # Sustituir el valor
        raiz.valor = sucesor.valor

        # Eliminar el sucesor original
        raiz.derecha = eliminar(raiz.derecha, sucesor.valor)

    return raiz


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.valor, end=" " )
        inorden(raiz.derecha)


# Pruebas
raiz = None

for valor in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, valor)

print("Árbol original:")
inorden(raiz)

print("\nEliminar hoja (20):")
raiz = eliminar(raiz, 20)
inorden(raiz)

print("\nEliminar nodo con un hijo (30):")
raiz = eliminar(raiz, 30)
inorden(raiz)

print("\nEliminar nodo con dos hijos (50):")
raiz = eliminar(raiz, 50)
inorden(raiz)
