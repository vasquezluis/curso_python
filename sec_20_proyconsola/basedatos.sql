CREATE DATABASE IF NOT EXISTS master_python;

USE master_python;

CREATE TABLE usuarios(
    id int(25) NOT NULL auto_increment,
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE notas(
    id int(25) NOT NULL auto_increment,
    usuario_id int(25) NOT NULL,
    titulo varchar(255) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDB;
