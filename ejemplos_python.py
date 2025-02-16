
# Conditional if…elif…else

notaIn=int(input("Introduzca nota: "))

if notaIn<5:
    calificacion="Suspenso"
else:
    calificacion="Aprobado"

print(calificacion)

# Evaluar si una variable contiene información

variable = 19

if variable:
    print("Contiene información")
else:
    print("No contiene información")

# Evaluar si una variable es True

if variable == True:
    print("Contiene información")
else:
    print("No contiene información")

# Verificar si un usuario es mayor de edad

edad=int(input("Introduce edad: "))

if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")

# Evaluar la calificación de un estudiante

nota=int(input("Introduce tu nota: "))

if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")

# Operador ternario

num = 12
var = "par" if (num % 2 == 0) else "impar"
print(var)

# Bucle for

for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)

# Validar email

miEmail=input("Introduce email")
email=False
for i in miEmail:
    if i=="@":
        email=True

if email:
    print("El email es correcto")
else:
    print("El mail no es correcto")

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
