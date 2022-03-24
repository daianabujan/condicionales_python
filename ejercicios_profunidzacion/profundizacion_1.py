# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input('Ingrese el primer número:\n'))
numero_2 = float(input('Ingrese el segundo número:\n'))

resta = numero_1 - numero_2
print('El resultado de restar', numero_1, 'y', numero_2, 'es', resta)

if resta > 0:
    print(resta, 'es positivo')
elif resta < 0:
    print(resta, 'es negativo')
else:
    print(resta, 'es cero')
