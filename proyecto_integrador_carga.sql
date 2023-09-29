USE proyecto_integrador;

INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("mago", "verde18", "mago@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("boris", "manzana12", "boris@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("cyborg", "galaxia20", "cyborg@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("loco", "ventana39", "loco@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("mami", "amor17", "mami@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("mafalda", "ver70", "mafalda@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("lolucho", "hermoso8", "lolucho@gmail.com");
INSERT INTO usuarios(nombre_usuario, contraseña, email) VALUES("gamer", "amarillo10", "gamer@gmail.com");

INSERT INTO servidores(nombre_servidor, descripcion) VALUES("literatura", "cuentos, novelas");
INSERT INTO servidores(nombre_servidor, descripcion) VALUES("juegos", "de accion");
INSERT INTO servidores(nombre_servidor, descripcion) VALUES("comidas", "recetas");

INSERT INTO canales(servidor_id, nombre_canal) VALUES(1, "cuentos");
INSERT INTO canales(servidor_id, nombre_canal) VALUES(1, "novelas");
INSERT INTO canales(servidor_id, nombre_canal) VALUES(2, "mario bros");
INSERT INTO canales(servidor_id, nombre_canal) VALUES(2, "sonic");
INSERT INTO canales(servidor_id, nombre_canal) VALUES(3, "milanesa napolitana");
INSERT INTO canales(servidor_id, nombre_canal) VALUES(3, "bomba de papa");

INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(4, 5, "como prepapar la milanesa");
INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(2, 3, "pasar etapas");
INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(1, 4, "juntar monedas");
INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(3, 2, "novelas de amor");
INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(5, 1, "cuentos de miedo");
INSERT INTO mensajes(usuario_id, canal_id, contenido) VALUES(6, 6, "como prepapar la bomba de papa");

INSERT INTO usuario_servidor(usuario_id, servidor_id) VALUES(6, 3);
INSERT INTO usuario_servidor(usuario_id, servidor_id) VALUES(5, 1);
INSERT INTO usuario_servidor(usuario_id, servidor_id) VALUES(3, 2);
INSERT INTO usuario_servidor(usuario_id, servidor_id) VALUES(7, 1);
