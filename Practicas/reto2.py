class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


# Prueba 1: Árbol vacío
vacio = None

# Prueba 2: Un solo nodo
un_nodo = Nodo(50)

# Prueba 3: Árbol de siete nodos
raiz = Nodo(50)
raiz.izquierda = Nodo(30)
raiz.derecha = Nodo(70)

raiz.izquierda.izquierda = Nodo(20)
raiz.izquierda.derecha = Nodo(40)

raiz.derecha.izquierda = Nodo(60)
raiz.derecha.derecha = Nodo(80)


# Mostrar resultados
for nombre, arbol in [
    ("Árbol vacío", vacio),
    ("Un nodo", un_nodo),
    ("Siete nodos", raiz)
]:
    print(nombre)
    print("Nodos:", contar_nodos(arbol))
    print("Hojas:", contar_hojas(arbol))
    print("Altura:", altura(arbol))
    print()