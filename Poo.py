class ListaEstructurada:
    def __init__(self):
        self.lista = []
        self.n_elementos = 0  # Contador de elementos en la lista

    def insertar(self, elemento):
        self.lista += [elemento]
        self.n_elementos += 1

    def eliminar(self, elemento):
        for i in range(self.n_elementos):
            if self.lista[i] == elemento:
                for j in range(i, self.n_elementos - 1):
                    self.lista[j] = self.lista[j + 1]
                
                self.lista = self.lista[:-1]  # Reducir tamaño eliminando el último
                self.n_elementos -= 1
                return True
        return False

    def buscar(self, elemento):
        for i in self.lista:
            if i == elemento:
                return True  # Retorna True si encuentra el elemento
        return False  # Retorna False si no encuentra el elemento

    def recorrer(self, function= print):
        for j in range(self.n_elementos):  # Corregir nItems a n_elementos
            function(self.lista[j])  # Corregir self[j] a self.lista[j]

    def ordenar(self):
        for i in range(self.n_elementos):
            for j in range(self.n_elementos - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

max_size = 3
arr = ListaEstructurada()  # Cambiar Array por ListaEstructurada
arr.insertar(77)
arr.insertar("abc")
arr.insertar(3)
arr.recorrer()

# Llamar al método buscar
print(arr.buscar(77))  # Retorna: True
print(arr.buscar("xyz"))  # Retorna: False

max_size = 3
arr = ListaEstructurada()  # Cambiar Array por ListaEstructurada
arr.insertar(77)
arr.insertar("abc")
arr.insertar(3)
arr.recorrer()
arr.buscar(3)