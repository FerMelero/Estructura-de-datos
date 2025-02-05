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
square= Power()
root= Power(0.5)
print("square.of(3) =", square.of(3))
print("root.of(3) =", root.of(3))

###


real_root = RealPower(0.5)
print("real_root.of(3) =", real_root.of(3))

print("real_root.of(-3)", real_root.of(-3))