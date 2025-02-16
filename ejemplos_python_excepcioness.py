

# -------------------------------
# Ejemplos de estructuras de control en Python
# -------------------------------

# Condicional if…elif…else
notaIn=int(input("Introduzca nota:"))

if notaIn<5:
    calificacion="Suspenso"
else:
    calificacion="Aprobado"

print(calificacion)

# Bucle for
for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)

# Bucle while
edad = 0
while edad < 18:  
    edad += 1
print("Tienes "+str(edad))

# Listas
miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1, 2]]

# Tuplas
miTupla = ("manzana", "banana", "cereza")

# Diccionarios
miDiccionario = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(miDiccionario)

# Sets
miSet = {"manzana", "banana", "cereza"}
miSet.add("naranja")

# Función para sumar valores
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valores(3, 5, 9, 4))

# Función recursiva para calcular factorial
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = 6
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')

# -------------------------------
# Ejemplos de manejo de excepciones en Python
# -------------------------------

# Capturando excepciones con try/except
def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 10)
except IndexError:
    print('Has puesto un índice muy grande.')

# Lanzando excepciones manualmente con raise
def verificar_numero(valor):
    if valor < 0:
        raise ValueError("El número no puede ser negativo")

try:
    verificar_numero(-5)
except ValueError as e:
    print(f"Error capturado: {e}")

# Uso de assert para depuración
a = 10
b = 0
assert a > b, "A tiene que ser mayor que B!"

# Creando una excepción personalizada
class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return str(self.mensaje)

try:
    raise MiError("Esto es un error personalizado")
except MiError as e:
    print(f"Capturado: {e}")

# Uso de try/finally
try:
    print("Abriendo archivo...")
finally:
    print("Esto siempre se ejecuta, cierre lo necesario.")

# Uso de try/except/else/finally
def dividir(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Fin del proceso.")

dividir(10, 2)
dividir(10, 0)

