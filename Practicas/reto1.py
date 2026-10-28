def preorden(raiz):
    if raiz is not None:
        print(raiz.valor, end=" ")
        preorden(raiz.izquierda)
        preorden(raiz.derecha)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.valor, end=" ")