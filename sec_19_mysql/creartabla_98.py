# importar conexion
from conexion_96 import *

cursor = database.cursor()

# crear tabla
cursor.execute("""

    CREATE TABLE IF NOT EXISTS vehiculos (
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10, 2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    );
""")

#ver tablas
cursor.execute("SHOW TABLES;")

for table in cursor:
    print(table)