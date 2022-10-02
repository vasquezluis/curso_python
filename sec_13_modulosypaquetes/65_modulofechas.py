# modulo de fechas

import datetime
from time import strftime

# mostrar la fecha de hoy
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%m/%d/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().time())

# ejemplo - imprimir parte de fecha en un reporte
fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
print("La fecha actual es:", fecha_actual)