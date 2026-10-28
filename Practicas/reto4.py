
class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.izquierda = None
        self.derecha = None


# Registrar un código
def registrar(raiz, codigo):
    if raiz is None:
        return Nodo(codigo)

    if codigo < raiz.codigo:
        raiz.izquierda = registrar(raiz.izquierda, codigo)
    elif codigo > raiz.codigo:
        raiz.derecha = registrar(raiz.derecha, codigo)

    return raiz


# Consultar un código
def consultar(raiz, codigo):
    if raiz is None:
        return False

    if raiz.codigo == codigo:
        return True

    if codigo < raiz.codigo:
        return consultar(raiz.izquierda, codigo)

    return consultar(raiz.derecha, codigo)


# Listar códigos ordenadamente
def listar(raiz):
    if raiz is not None:
        listar(raiz.izquierda)
        print(raiz.codigo)
        listar(raiz.derecha)


# Retirar un código
def retirar(raiz, codigo):
    if raiz is None:
        return None

    if codigo < raiz.codigo:
        raiz.izquierda = retirar(raiz.izquierda, codigo)

    elif codigo > raiz.codigo:
        raiz.derecha = retirar(raiz.derecha, codigo)

    else:
        if raiz.izquierda is None:
            return raiz.derecha

        if raiz.derecha is None:
            return raiz.izquierda

        sucesor = raiz.derecha
        while sucesor.izquierda is not None:
            sucesor = sucesor.izquierda

        raiz.codigo = sucesor.codigo
        raiz.derecha = retirar(raiz.derecha, sucesor.codigo)

    return raiz


# Ejemplo
raiz = None

for codigo in [50, 30, 70, 20, 40, 60, 80]:
    raiz = registrar(raiz, codigo)

print("¿Existe el código 40?", consultar(raiz, 40))

print("Libros ordenados:")
listar(raiz)

raiz = retirar(raiz, 30)

print("Después de retirar el código 30:")
listar(raiz)
