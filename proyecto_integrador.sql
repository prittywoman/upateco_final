
CREATE DATABASE IF NOT EXISTS proyecto_integrador;

USE proyecto_integrador;

CREATE TABLE usuarios (
	usuario_id INT AUTO_INCREMENT PRIMARY KEY,
	nombre_usuario VARCHAR (100) NOT NULL,
    contraseña VARCHAR (100) NOT NULL,
    email VARCHAR (150) NOT NULL,
    foto_img VARCHAR (150)
);

CREATE TABLE servidores (
	servidor_id INT AUTO_INCREMENT PRIMARY KEY,
	nombre_servidor VARCHAR (150) NOT NULL,
    descripcion TEXT
);

CREATE TABLE canales (
	canal_id INT AUTO_INCREMENT PRIMARY KEY,
	nombre_canal VARCHAR (100) NOT NULL,
	servidor_id INT NOT NULL,
    constraint fk_canales_servidores FOREIGN KEY (servidor_id) REFERENCES servidores(servidor_id) ON DELETE CASCADE
);

CREATE TABLE mensajes (
	mensaje_id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT NOT NULL,
	canal_id INT NOT NULL,
	contenido TEXT NOT NULL,
	fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	constraint fk_mensajes_usuarios FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE,
  	constraint fk_mensajes_canales FOREIGN KEY (canal_id) REFERENCES canales(canal_id) ON DELETE CASCADE
);

CREATE TABLE usuario_servidor (
	id_usuario_servidor INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT NOT NULL,
	servidor_id INT NOT NULL,
  	UNIQUE(usuario_id, servidor_id),
  	CONSTRAINT fk_usuarios_servidores_associations_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE,
  	CONSTRAINT fk_usuarios_servidores_associations_servidor FOREIGN KEY (servidor_id) REFERENCES servidores(servidor_id) ON DELETE CASCADE
);    
