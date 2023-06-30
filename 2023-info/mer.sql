
-- Active: 1686015002714@@127.0.0.1@3306
CREATE DATABASE pabloruido;
USE pabloruido;
SHOW tables;
SHOW DATABASES;

USE pabloruido;

CREATE TABLE blog(
    nombre CHAR(20),
    url CHAR (255),
    PRIMARY KEY (nombre)
);

SELECT *
FROM blog;  -- se consulta la TABLa    

INSERT blog (nombre, url) VALUES ("el asombroso blog", "wwwww.blogdemusicinglishchaco.com")

SELECT *
FROM blog;

CREATE TABLE articulo (
    id INT AUTO_INCREMENT,
    titulo CHAR (20),
    imagen CHAR (255),
    fecha_publicacion DATE,
    contenido TEXT,
    estado CHAR (20) CHECK (estado = "activo" OR estado = "inactivo"),
    resumen CHAR (250),
    nombre_blog CHAR (20),
    PRIMARY KEY (id),
    FOREIGN KEY (nombre_blog) REFERENCES blog (nombre)
);

INSERT articulo(
    titulo,
    imagen,
    fecha_publicacion,
    contenido,
    estado,
    resumen,
    nombre_blog
) VALUES(
    "Django",
    "ajadjadjdaj",
    "2023-06-06",
    "fsfjfjsjf sjfjsfj jsfj j",
    "activo",
    "el resumen",
    "el asombroso blog"
);

SELECT *
FROM articulo;

CREATE TABLE colaborador(
    dni INT,
    nombre CHAR (20),
    apellido CHAR (20),
    estado CHAR (8) CHECK (estado = "activo" OR estado = "inactivo"),
    fecha_reg DATETIME DEFAULT CURRENT_TIMESTAMP,
    email CHAR (25) NOT NULL,
    telefono INT,
    avatar CHAR (255),
    contraseña CHAR (30),
    PRIMARY KEY (dni)
);

INSERT colaborador (
    dni,
    nombre,
    apellido,
    estado,
    email,
    telefono,
    avatar,
    contraseña
) VALUES(
    37704290,
    "pablo",
    "ruido",
    "activo",
    "pabloruido@hotmail.com",
    36248966,
    "afhafhfhfhsfhf",
    "pabloutittoo"
);

