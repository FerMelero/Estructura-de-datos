class BinarySearch:
    def __init__(self, a):
        self.__a = sorted(a)
        self.__nitems = len(a)

    def find(self, item):
        lo = 0
        hi = self.__nitems - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] < item:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1  # Devuelve -1 si el elemento no se encuentra


class OrderedArray(object):
    def __init__(self, initialSize): # constructor
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n < self.__nItems:  # Corrección en la condición
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def find(self, item):
        lo = 0
        hi = self.__nItems - 1  # Corrección en el uso de __nItems

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] < item:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1  # Devuelve -1 si el elemento no se encuentra

    def search(self, item):
        index = self.find(item)
        if index != -1 and self.__a[index] == item:  # Corrección en la verificación del índice
            return self.__a[index]
        return None

    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")

        i = 0
        while i < self.__nItems and self.__a[i] < item:
            i += 1

        for j in range(self.__nItems, i, -1):
            self.__a[j] = self.__a[j-1]

        self.__a[i] = item
        self.__nItems += 1

    def delete(self, item):
        j = self.find(item)
        if j != -1 and j < self.__nItems and self.__a[j] == item:
            # Desplaza los elementos hacia la izquierda para cubrir el hueco dejado por el elemento eliminado
            for k in range(j, self.__nItems - 1):
                self.__a[k] = self.__a[k + 1]
            # Disminuye el número de elementos
            self.__nItems -= 1
            # Establece el último elemento a None (opcional, depende de la implementación)
            self.__a[self.__nItems] = None
            return True
        return False

# Uso del OrderedArray
maxSize = 11
arr = OrderedArray(maxSize)
arr.insert(1)
arr.insert(2)
arr.insert(3)
arr.insert(4)
arr.insert(2)  # Repetición del número 2
arr.insert(5)
arr.insert(6)
arr.insert(7)
arr.insert(8)
arr.insert(1)  # Repetición del número 1
arr.insert(9)
print(len(arr))
print(arr)

print(arr.find(2))
print(arr.find(3))

def identity(tupla):
    return tupla[1]

class OrderedRecordArray:
    def __init__(self, initialSize, key = identity):
        self.__a = [None] * initialSize
        self.__nItems = 0
        self.__key = key

    def find(self, key):
        low = 0
        high = len(self.__a) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]) < key:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def insert(self, record):
        if len(self.__a) >= self.__maxsize:
            raise Exception("El arreglo está lleno, no se pueden insertar más elementos.")
        index = self.find(self.__key(record))
        self.__a.insert(index, record)

    def delete(self, key):
        index = self.find(key)
        if index < len(self.__a) and self.__key(self.__a[index]) == key:
            self.__a.pop(index)

    def __getitem__(self, index):
        return self.__a[index]

    def __len__(self):
        return len(self.__a)

    def __str__(self):
        return str(self.__a)



# Definir la función clave para extraer el número de la tupla
def key_function(tupla):
    return tupla[1]  # Extrae el segundo elemento de la tupla (el número)
'''
# Crear el arreglo ordenado con un tamaño máximo de 10
maxsize = 10
array = OrderedRecordArray(maxsize, key_function)

# Insertar tuplas ("letra", num)
array.insert(("A", 3))
array.insert(("B", 1))
array.insert(("C", 2))

# El arreglo estará ordenado por el número (num)
print(array)  # Salida: [('B', 1), ('C', 2), ('A', 3)]
'''
