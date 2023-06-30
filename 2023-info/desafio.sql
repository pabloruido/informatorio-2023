-- Active: 1686015002714@@127.0.0.1@3306@pabloruido

-- Disponemos el siguiente modelo lógico para gestionar la información del blog de una
--ONG.
--Debes escribir los comandos SQL que permitan la creación de las tablas con sus
--respectivas restricciones de claves primarias y foráneas.
--- Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol
--de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos:
--es_publico, es_colaborador y es_admin son booleanos.

--- Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
--estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
--Booleano.
--- Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.
--- Agregar el comando necesario que introduzca 3 comentarios al primer artículo
--agregado y 2 comentarios al segundo artículo.
--- Agregar el comando necesario para listar todos los artículos que tengan
--comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
--nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
--comentario, agrupados por artículos.

CREATE DATABASE pabloruido;

USE  pabloruido;

CREATE TABLE usuario (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR (50),
    apellido VARCHAR (50),
    telefono INT,
    username VARCHAR (50),
    email VARCHAR (50),
    contraseña VARCHAR (50),
    estado BOOLEAN,
    fecha_creacion DATE,
    avatar VARCHAR (255),
    es_publico BOOLEAN,
    es_colaborador BOOLEAN,
    es_admin BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE articulo (
    id INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    titulo VARCHAR (50),
    resumen VARCHAR (255),
    contenido TEXT,
    fecha_publicacion DATE,
    estado  BOOLEAN,
    imagen VARCHAR (255),
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id)
);

CREATE TABLE comentario (
    id INT NOT NULL AUTO_INCREMENT,
    id_articulo INT NOT NULL,
    id_usuario INT NOT NULL,
    contenido TEXT,
    fecha_hora DATETIME,
    estado BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (id_articulo) REFERENCES articulo (id),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id)
);

CREATE TABLE categoria (
    id INT NOT NULL AUTO_INCREMENT,
    id_categoria INT NOT NULL,
    nombre VARCHAR (20),
    descripcion TEXT,
    imagen VARCHAR (255),
    estado BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);

CREATE TABLE categoria_articulo (
    id_articulo INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_articulo) REFERENCES articulo (id),
    FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo",
    "ruido",
    35824995,
    "pabloruido",
    "pabloruido@hotmail.com",
    "pasffaspfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    0,
    0,
    1
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo2",
    "ruido2",
    35824995,
    "pabloruido2",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    0,
    1,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo3",
    "ruido3",
    35824995,
    "pabloruido2",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    0,
    1,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo4",
    "ruido4",
    35824995,
    "pabloruido2",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    0,
    1,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo5",
    "ruido5",
    35824995,
    "pabloruido2",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    0,
    1,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo6",
    "ruido6",
    35824995,
    "pabloruido6",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    1,
    0,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo7",
    "ruido7",
    35824995,
    "pabloruido7",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    1,
    0,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo8",
    "ruido8",
    35824995,
    "pabloruido8",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    1,
    0,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo14",
    "ruido14",
    35824995,
    "pabloruido14",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    1,
    0,
    0
);

INSERT usuario (
    nombre,
    apellido,
    telefono, 
    username,
    email,
    contraseña, 
    estado, 
    fecha_creacion, 
    avatar, 
    es_publico, 
    es_colaborador,
    es_admin
) VALUES (
    "pablo16",
    "ruido16",
    35824995,
    "pabloruido4416",
    "pabloreuido@hotmail.com",
    "pasffaespfp",
    1,
    "2023-06-06",
    "ajsfjasfjfsfasjsfj",
    1,
    0,
    0
);

--- Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios
--agregado con rol de colaborador.

UPDATE usuario SET es_admin = 1 where id = 2;

--- Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
--estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
--Booleano.

INSERT articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado,imagen) VALUES (1, "EL BOSQUE", "un asombroso relato", "habla del bosque", "2022-05-03", 1,"ww.w.w.imagen.com");

INSERT articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado,imagen) VALUES (2, "la selva", "un asombroso relato", "habla de la selva", "2022-07-03", 1,"ww.w.w.imagen2.com");

INSERT articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado,imagen) VALUES (3, "la mosca", "un insecto", "habla de la selva", "2022-01-03", 1,"ww.w.w.imagen23.com");

INSERT articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado,imagen) VALUES (3, "racing", "relato de pasion", "el escudo", "2023-01-03", 0,"ww.w.w.imagen223.com");

--- Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.

DELETE FROM articulo where estado = 0;

-- Agregar el comando necesario que introduzca 3 comentarios al primer artículo
--agregado y 2 comentarios al segundo artículo.

INSERT comentario (id_articulo, id_usuario, contenido, fecha_hora, estado) VALUES (1, 5, "muy buen blog", "2023-06-06 14:00", 1);
INSERT comentario (id_articulo, id_usuario, contenido, fecha_hora, estado) VALUES (1, 6, "horrible lo que escribis", "2023-06-06 17:00", 1);
INSERT comentario (id_articulo, id_usuario, contenido, fecha_hora, estado) VALUES (1, 8, "viva yo!", "2023-07-06 08:15", 1);
INSERT comentario (id_articulo, id_usuario, contenido, fecha_hora, estado) VALUES (2, 8, "viva yo de nuevo!", "2023-07-06 18:15", 1);
INSERT comentario (id_articulo, id_usuario, contenido, fecha_hora, estado) VALUES (2, 4, "HOLA Soy nuevo en tu blog", "2023-05-06 18:15", 1);

--- Agregar el comando necesario para listar todos los artículos que tengan
--comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
--nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
--comentario, agrupados por artículos.

SELECT comentario.contenido, articulo.titulo, articulo.fecha_publicacion, usuario.username, comentario.fecha_hora FROM articulo, comentario, usuario WHERE comentario.id_usuario = usuario.id and articulo.id = comentario.id_articulo;

