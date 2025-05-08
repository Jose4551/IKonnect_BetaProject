create database Ikonnect;
-- 2.2. Tabla de usuarios
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  telefono VARCHAR(20) UNIQUE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2.3. Tabla de mensajes
CREATE TABLE mensajes (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  contenido TEXT NOT NULL,
  enviado_at DATETIME NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3.1. Usuarios de prueba
INSERT INTO usuarios (nombre, telefono) VALUES
  ('Ana Pérez', '+5213312345678'),
  ('Carlos López', '+5213312345679'),
  ('Beatriz Sánchez', '+5213312345680'),
  ('David Torres', '+5213312345681');

-- 3.2. Mensajes de prueba
INSERT INTO mensajes (usuario_id, contenido, enviado_at) VALUES
  (1, '¡Hola a todos!',      '2025-05-01 08:15:00'),
  (2, 'Buenos días, Ana.',    '2025-05-01 08:16:30'),
  (3, '¿Cómo están?',         '2025-05-01 09:00:00'),
  (1, 'Bien, gracias. ¿Ustedes?', '2025-05-01 09:02:15'),
  (4, 'Aquí listos para la reunión.', '2025-05-01 09:05:00'),
  (2, 'Perfecto. Empezamos en 10min.',  '2025-05-01 09:10:00'),
  (1, 'Genial.',              '2025-05-01 09:11:45'),
  (3, '¿Alguien lleva la minuta?',    '2025-05-01 10:30:00'),
  (4, 'Yo la tengo, la comparto luego.', '2025-05-01 10:32:20'),
  (2, 'Gracias, David.',      '2025-05-01 10:33:10'),
  (1, 'Qué tema tan interesante.', '2025-05-02 14:20:00'),
  (3, 'Totalmente de acuerdo.',   '2025-05-02 14:21:50'),
  (2, 'Voy a revisar el documento.', '2025-05-02 16:00:00'),
  (4, '¿Alguien disponible para llamada?', '2025-05-03 11:00:00'),
  (1, 'Yo en 5 minutos.',     '2025-05-03 11:02:30'),
  (2, 'Perfecto, aviso cuando listo.', '2025-05-03 11:05:00'),
  (3, 'Listo para llamada.',  '2025-05-03 11:06:40'),
  (4, 'Iniciando ahora.',     '2025-05-03 11:07:00'),
  (1, 'Gracias a todos.',     '2025-05-04 17:45:00'),
  (2, 'Hasta luego.',         '2025-05-04 17:46:10');