class Power(object):
    # Atributo de clase que define el exponente por defecto
    default_exponent = 2
    
    # El constructor (__init__) inicializa el objeto con un exponente dado,
    # si no se pasa uno, se usa el valor por defecto (2)
    def __init__(self, exponent=default_exponent):
        self.exponent = exponent  # Asigna el valor del exponente al objeto
    
    # Método que calcula x elevado al exponente de la clase
    def of(self, x):
        return x ** self.exponent  # Retorna x a la potencia del exponente

# Definición de una subclase que hereda de Power
class RealPower(Power):
    # Sobrescribe el método 'of' para realizar una comprobación adicional
    def of(self, x):
        # Si el exponente es un entero o x es mayor o igual a 0, realiza la operación
        if isinstance(self.exponent, int) or x >= 0:
            return x ** self.exponent
        
        # Si x es negativo y el exponente es fraccionario (no entero),
        # lanza un error porque las raíces fraccionarias de números negativos
        # no son números reales
        raise ValueError("Fractional powers of negative numbers are imaginary")

print("Power.default_exponent:", Power.default_exponent)
square = Power()
root = Power(0.5)
print("square.of(3) =", square.of(3))
print("root.of(3) =", root.of(3))

real_root = RealPower(0.5)
print("real_root.of(3) =", real_root.of(3))

try:
    print("real_root.of(-3) =", real_root.of(-3))  # Simular error
except ValueError as e:
    print(e)

class Array:
    def __init__(self, maxSize):
        self.__a = [None] * maxSize  # Atributo privado
        self.__nItems = 0  # Atributo privado

    def __len__(self):
        return self.__nItems

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def search(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return self.__a[j]
        return None

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    # Método getter para acceder a __nItems
    def get_nItems(self):
        return self.__nItems

    # Método setter para modificar __nItems (opcional, dependiendo de si quieres permitir modificaciones)
    def set_nItems(self, value):
        if value >= 0 and value <= len(self.__a):
            self.__nItems = value
        else:
            raise ValueError("El valor de nItems debe estar dentro del rango válido.")

arr = Array(100)

arr.insert(77)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
arr.traverse()