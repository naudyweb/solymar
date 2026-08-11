<?php
// Copia este archivo a config.php y completa los valores reales.
// config.php NO se sube a git (ver .gitignore) porque contiene la clave de acceso.

// 1) Genera el hash de la clave compartida del personal con este comando:
//    php -r "echo password_hash('tu-clave-aqui', PASSWORD_DEFAULT), PHP_EOL;"
//    y pega el resultado abajo.
define('RESERVAS_PASSWORD_HASH', '$2y$10$reemplaza.esto.con.el.hash.generado.arriba');

// 2) Ruta al archivo SQLite donde se guardan las reservas (se crea solo si no existe).
define('RESERVAS_DB_PATH', __DIR__ . '/data/reservas.sqlite');
