# ejercicio 10

"""

    Pedir la nota de 15 alumnos y sacar cuantos han aprobado o suspendido

"""

alumno = []

for i in range(0,15):
    alumno.append(int(input(f"Ingresa la nota del estudiante {i+1}: ")))

print('\n')

for i in range(0,15):
    if alumno[i] < 60:  
        print(f"El alumno {i+1} no esta aprobado :(")
    elif alumno[i] > 60 and alumno[i] <= 100:
        print(f"El alumno {i+1} esta aprobado :)")
    elif alumno[i] > 100 or alumno[i] < 0:
        print(f"El alumno {i+1} no tiene una nota valida")